from tkinter import *
from tkinter.ttk import *
import random

root=Tk()
root.geometry("500x500")

r=random.randint(0,255)
g=random.randint(0,255)
b=random.randint(0,255)
frame=Frame(root,width=45,height=45)
scrollbar=Scrollbar(frame)
listbox=Listbox(frame,yscrollcommand=scrollbar.set)
for i in range(101):
    listbox.insert(END,str(i))

frame.pack(anchor=CENTER)
scrollbar.pack(anchor=CENTER,side=RIGHT,fill=Y)
listbox.pack(anchor=CENTER,side=RIGHT)
scrollbar.config(command=listbox.yview)
root.mainloop()