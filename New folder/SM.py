class SM:
    def start(self):
        self.state = self.startState
    def step(self, inp):
        (s,o) = self.getNextValues(self.state,inp)
        self.state = s
        return o
    def transduce(self, inputs):
        self.start()
        return [self.step(inp) for inp in inputs]


class Accumulator(SM):
    startState = 0
    def getNextValues(self, state, inp):
        return (state + inp, state+inp)

    
class Cascade(SM):
    startState = 0
    def __init__(self, m1,m2, name=None):
        self.m1 = m1
        self.m2 = m2
        
    def transduce(self, inputs):
        self.start()
        self.m1.start()
        self.m2.start()
        x = [self.m1.step(inp) for inp in inputs]
        return [self.m2.step(i) for i in x]

a = Accumulator()
b = Accumulator()
c = Cascade(a,b)

print(c.transduce([7,3,4]))

