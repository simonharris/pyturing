from pyturing import Tape


class TestTape:

    def setup_method(self):
        self.tape = Tape()

    def test_write_read(self):

        self.tape[1] = 'A'
        assert(self.tape[1] == 'A')

        self.tape[1000] = 'B'
        assert(self.tape[1000] == 'B')

        self.tape[-10] = 'C'
        assert(self.tape[-10] == 'C')

    def test_defaults(self):
        assert(self.tape[0] == '')
        assert(self.tape[-123] == '')
        assert(self.tape[123] == '')

    def test_prepopulate(self):
        input = '1111'
        self.tape.populate(input)
        assert(self.tape[-1] == '')
        assert(self.tape[0] == '1')
        assert(self.tape[1] == '1')
        assert(self.tape[2] == '1')
        assert(self.tape[3] == '1')
        assert(self.tape[4] == '')
