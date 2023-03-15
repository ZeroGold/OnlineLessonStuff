class getSet:
    def __init__(self):
        self.x = None
    def setVar(self, *args):
        self.x = [arg for arg in args]
    def getVar(self):
        if len(self.x) == 1:
            return self.x[0]
        else:
            return self.x








