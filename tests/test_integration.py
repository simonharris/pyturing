import json

from pyturing import Head, Tape, Machine, Program


class TestExecution:

    def test_increment(self):

        init = '1111' # 4 in unary

        with open('tests/programs/increment.json') as fh:
            code = json.load(fh)

        machine = Machine(Head(Tape(init)))
        machine.load(Program(code))
        machine.run()

        assert str(machine.get_tape()) == '11111' # 5 in unary
