from collections import defaultdict
from dataclasses import dataclass

class Tape(defaultdict):

    def __init__(self):
        super().__init__(lambda: '')


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

