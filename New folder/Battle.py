from SM import SM
class Battle(SM):
    startState = "wait"
    def getNextValues(self, state, inp):
        if inp == "attack":
            print("Swing")
            return ("attack", "wait")
        if inp ==  "defend":
            print("Block")
            return ("defend", "wait")
        if inp == "evade":
            print("Duck")
            return("evade", "wait")
        else:
            print("Will improve upon later")




class Character():
    

x = Battle()
x.transduce(["attack","attack","evade","defend","attack","evade"])
print(x.state)
            
            
            
