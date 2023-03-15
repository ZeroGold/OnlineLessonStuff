#### SAMPLE GAME
from tkinter import *
from getSet import getSet
i =  Tk()
v = getSet()
game =  True
frame = Frame(i)
frame.pack()
button = Button(i,text="Mint", command = lambda:change(1))
button2 = Button(i,text="Login", command = lambda:change(2))
button.pack()
button2.pack()
def change(x):
    v.setVar(x)
    #i.quit()
def window():
    i.deiconify()
    i.mainloop()
def main():
    while game:
        i.deiconify()
        i.mainloop()      
        if v.getVar() == 1:
            #i.withdraw()
            break
        if v.getVar() == 2:
            i.withdraw()
            break
main() 
