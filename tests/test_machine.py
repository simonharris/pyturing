import json
from unittest.mock import MagicMock

from pyturing import Machine, Program


class TestMachine():

    def setup_method(self):
        with open('tests/programs/01.json') as fh:
            data = json.load(fh)
        self.program = Program(data)
        self.mockhead = MagicMock()
        self.machine = Machine(self.mockhead)
        self.machine.load(self.program)

    def test_initialisation(self):
         self.mockhead.move_right.assert_not_called()
         self.mockhead.move_left.assert_not_called()

    def test_machine(self):
        # "state0012": {
        #   "0": {
        #     "next": "state0042",
        #     "write": 1,
        #     "move": "R"

        self.mockhead.read.return_value = '0'
        self.machine.step()

        assert self.mockhead.move_right.call_count == 1
        self.mockhead.write.assert_called_once_with('1')
        assert self.machine.get_state() == 'state0042'
