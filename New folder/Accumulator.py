class Accumulator(SM):
    startState = 0
    def getNextValues(self, state, inp):
        return (state + inp, state+inp)
