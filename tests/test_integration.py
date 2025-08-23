import json

from pyturing import Head, Tape, Machine, Program


class TestExecution:

    def test_increment(self):

        init = '1111' # 4 in unary
        code = self._read_code('tests/programs/increment.json')

        machine = Machine(Head(Tape(init)))
        machine.load(Program(code))
        machine.run()

        assert str(machine.get_tape()) == '11111' # 5 in unary


    def test_add_two(self):

        init = '1111_111' # 4+3 in unary
        code = self._read_code('tests/programs/add_two.json')

        machine = Machine(Head(Tape(init)))
        machine.load(Program(code))
        machine.run()

        assert str(machine.get_tape()) == '1111111' # 7 in unary


    def _read_code(self, filename):
        with open(filename) as fh:
            code = json.load(fh)
        return code
