from pyturing import Transition

class TestTransition:

    def test_accessors(self):

        spec = {'next':'s00012', 'write':1, 'move':'R'}

        inst = Transition(**spec)
        assert(inst.next_state() == 's00012')
        assert(inst.to_write() == 1)
        assert(inst.next_move() == 'R')
