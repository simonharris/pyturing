import json
from pprint import pprint

from pyturing import Program, Transition


class TestProgram:

    def setup_method(self):
        with open('tests/programs/01.json') as fh:
                data = json.load(fh)
        self.program = Program(data)

    def test_initialisation(self):
        assert self.program.get_initial_state() == 'state0012'

    def test_get_transitions(self):

        tr = self.program.get_transition('state0042', '1')

        assert isinstance(tr, Transition)
        assert tr.next_state() == 'state0012'
        assert tr.to_write() == 0
        assert tr.next_move() == 'L'

# TODO: what if no istruction for a state/read combination?
