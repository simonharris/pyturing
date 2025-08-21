from pyturing import Head, Tape


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


class TestHead:

    def setup_method(self):
        self.tape = Tape()
        self.head = Head(self.tape)

        self.tape[0] = 'A'
        self.tape[-2] = 'B'
        self.tape[2] = 'C'

    def test_defaults(self):
        assert(self.head.read() == 'A')

    def test_shift_and_read(self):
        self.head.move_left()
        self.head.move_left()
        assert(self.head.read() == 'B')
        self.head.move_right()
        self.head.move_right()
        self.head.move_right()
        self.head.move_right()
        assert(self.head.read() == 'C')

    def test_write_and_read(self):
        self.head.write('Q')
        assert(self.head.read() == 'Q')
        self.head.move_right()
        self.head.move_right()
        self.head.write('Z')
        assert(self.head.read() == 'Z')
        self.head.move_left()
        self.head.move_left()
        assert(self.head.read() == 'Q')
        self.head.move_right()
        self.head.move_right()
        assert(self.head.read() == 'Z')
