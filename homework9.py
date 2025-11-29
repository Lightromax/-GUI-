from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import*
import random
######################################################################################################
root=Tk()
root.title("Guess the multiplication?")
root.geometry("600x500")
#######################################################################################################
#defining
comp1=random.randint(1,7)
comp2=random.randint(1,7)
number=comp1*comp2
def guess():
    num1=int(guessbox1.get())
    num2=int(guessbox2.get())
    if num1 == comp1 and num2 == comp2:
        root.destroy()
        showinfo("Message3","You win")
    if num1 == comp2 and num2 == comp1:
        root.destroy()
        showinfo("Message3","You win")
    if num1 > comp1 and num2 > comp2:
        if num1 != comp2 and num2  != comp1:
            showinfo("Message2","Too high")
    if num1 < comp1 and num2 > comp2:
        if num1 != comp2 and num2  != comp1:
            showinfo("Message2","num1 too low num2 too high")
    if num1 > comp1 and num2 < comp2:
        if num1 != comp2 and num2  != comp1:
            showinfo("Message2","num1 too high num2 too low")
    if num1 < comp1 and num2 < comp2:
        if num1 != comp2 and num2  != comp1:
            showinfo("Message2","Too low")
def name():
    aname=namebox.get()
    showinfo("Message1","OK "+str(aname)+", Your number is "+str(number)+",guess two numbers that multiply to get this")
######################################################################################################
#creating
namelabel=Label(root,text="Whats your name:")
namebox=Entry(root)
enterbutton=Button(root,text="Enter",command=name)
guesslabel=Label(root,text="Take a guess of of the numbers could be")
guessbox1=Entry(root)
guessbox2=Entry(root)
guessbutton=Button(root,text="Guess",command=guess)
######################################################################################################
#Placing
namelabel.grid(row=1,column=1)
namebox.grid(row=1,column=2)
enterbutton.grid(row=1,column=3)
guesslabel.grid(row=2,column=1)
guessbox1.grid(row=2,column=2)
guessbox2.grid(row=2,column=3)
guessbutton.grid(row=2,column=4)

root.mainloop()