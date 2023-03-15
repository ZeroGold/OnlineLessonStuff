class Delay:
    def __init__(self):
        self.delay = 0
        self.output = []

    def Adder(self, x):
        return x+self.delay
    def Delay(self, x):
        self.delay = x*-1

    def Input(self, args):
        for arg in args:
            self.output.append(self.Adder(arg))
            self.Delay(arg)
        



            


x = Delay()
x2 = Delay()


y = [0,0,1,0]
x.Input(y)
x2.Input(x.output)
print(x.output)
print(x2.output)





#  y[n] = x[n] - x[n-1]



class Right:
    def __init__(self):
        self.output = []


    
