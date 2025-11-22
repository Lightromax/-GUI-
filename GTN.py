from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *
import random

root=Tk()
root.config(background="grey")
root.title("guess the number")
root.geometry("500x500")

def name():
    Name=Name_box.get()
    showinfo("Messagebox1","Well, "+Name+",I am thinkin of a number from 1-20! Can you help me guess it.")

number=random.randint(1,20)

def checknum():
    guess=Guess_box.get()
    guess=int(guess)
    if guess > number:
        showinfo("Messagebox","Guess is to High")
    if guess < number:
        showinfo("Messagebox2","Guess is to Low")
    if guess == number:
        showinfo("Messagebox3","Correct")

Title_label=Label(root,text="Welcome to our game",background="grey")
Namequestion_label=Label(root,text="What is your name?",background="grey")
Name_box=Entry(root)
Enter_button=Button(root,text="Enter",command=name)
Guess_label=Label(root,text="Have a guess:",background="grey")
Guess_box=Entry(root)
Guess_button=Button(root,text="Guess",command=checknum)

Title_label.grid(row=1,column=1)
Namequestion_label.grid(row=2,column=1)
Name_box.grid(row=3,column=1)
Enter_button.grid(row=3,column=8)
Guess_label.grid(row=4,column=1)
Guess_box.grid(row=6,column=1)
Guess_button.grid(row=6,column=8)

root.mainloop()