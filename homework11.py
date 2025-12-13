from tkinter import *
from tkinter.ttk import *
##########################################################
#Screen
root=Tk()
root.geometry("550x400")
#Variables
operators=["+","-","x","/"]
##########################################################
def solve():
    num1=int(box1.get())
    num2=int(box2.get())
    op=str(op_combo.get())
    if op == "+":
        plus=num1 + num2
        answer.config(text="Your answer is "+str(plus))
    if op == "-":
        sub=num1 - num2
        answer.config(text="Your answer is "+str(sub))
    if op == "x":
        mul=num1 * num2
        answer.config(text="Your answer is "+str(mul))
    if op == "/":
        div=num1 / num2
        answer.config(text="Your answer is "+str(div))
##########################################################
#Creating
box1=Entry(root)
box2=Entry(root)
op_combo=Combobox(root,values=operators)
solve_button=Button(root,text="Solve",command=solve)
answer=Label(root,text="")
##########################################################
#Placing
box1.place(x=50,y=200)
box2.place(x=350,y=200)
op_combo.place(x=200,y=200)
solve_button.place(x=250,y=300)
answer.place(x=200,y=100)


root.mainloop()