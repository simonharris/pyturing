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
        assert(self.tape[123] == '')
