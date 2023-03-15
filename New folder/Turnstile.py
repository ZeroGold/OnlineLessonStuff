class Turnstile(SM):
    startState = "locked"

    def getNextVales(self, state, inp):
        if inp == "coin":
            return ("unlocked", "enter")
        if inp == "turn":
            return ("locked", "pay")
        if inp == "locked":
            return ("locked", "pay")
        else:
            return ("unlocked", "enter")
