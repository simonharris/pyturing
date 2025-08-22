from pprint import pprint

from collections import defaultdict
from dataclasses import dataclass


class Tape(defaultdict):

    def __init__(self, initial:str = ''):
        super().__init__(str)

    def populate(self, input:str):
        self.update(enumerate(input))


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

    next: str
    write: str
    move: str

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

    def load(self, program: Program):
        self.program = program
        self.state = self.program.get_initial_state()

    def get_state(self) -> str:
        return self.state

    def step(self):
        input = self.head.read()
        tr = self.program.get_transition(self.state, input)
        self.head.write(tr.to_write())
        self.state = tr.next_state()

        if tr.next_move() == 'R':
            self.head.move_right()
        elif tr.next_move() == 'L':
            self.head.move_left()
