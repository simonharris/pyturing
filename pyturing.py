from pprint import pprint

from collections import defaultdict
from dataclasses import dataclass


STATE_HALT = 'HALT'
CELL_BLANK = '_'


class Tape(defaultdict):

    def __init__(self, initial:str = ''):
        super().__init__(lambda: '_')
        self.populate(initial)

    def populate(self, input:str):
        self.update(enumerate(input))

    def __str__(self):
        return ''.join(self.values())


class Head():

    def __init__(self, tape: Tape):
        self.ctr = 0
        self.tape = tape

    def read(self):
        return self.tape[self.ctr]

    def move_left(self):
        self.ctr -= 1

    def move_right(self):
        self.ctr += 1

    def write(self, value):
        self.tape[self.ctr] = value


@dataclass
class Transition():

    next: str = None
    write: str = None
    move: str = None

    def next_state(self) -> str:
        return self.next

    def to_write(self) -> str:
        return self.write

    def next_move(self) -> str:
        return self.move


class Program():

    def __init__(self, data):
        self.initial_state = data['initialState']
        self.transitions = data['transitions']

    def get_initial_state(self):
        return self.initial_state

    def get_transition(self, state: str, readval: str) -> Transition:
        return Transition(**self.transitions[state][readval])


class Machine():

    def __init__(self, head: Head):
        self.head = head
        self.state = STATE_HALT

    def load(self, program: Program):
        self.program = program
        self.state = self.program.get_initial_state()

    def get_state(self) -> str:
        return self.state

    def step(self):
        input = self.head.read()
        tr = self.program.get_transition(self.state, input)

        if write := tr.to_write():
            self.head.write(write)

        if state := tr.next_state():
            self.state = state

        if tr.next_move() == 'R':
            self.head.move_right()
        elif tr.next_move() == 'L':
            self.head.move_left()

    def run(self):
        while self.state != STATE_HALT:
            self.step()

    def get_tape(self):
        return self.head.tape
