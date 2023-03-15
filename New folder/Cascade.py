import SM
class Cascade(SM):
    def __init__(self, m1,m2, name=None):
        self.m1 = m1
        self.m2 = m2
    def transduce(self, inputs):
        self.start()
        return [m2.step(m1.step(inp)) for inp in inputs]

a = Accumulator()
b = Accumulator()
c = Cascade(a,b)

print(c.transduce([1,2,3]))
