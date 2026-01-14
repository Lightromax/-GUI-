from tkinter import *
from tkinter.ttk import *
import random

root=Tk()
root.geometry("500x500")

r=random.randint(0,255)
g=random.randint(0,255)
b=random.randint(0,255)

def addcolor():
    color=add_box.get()
    listbox.insert(END,color)
def remove():
    select=listbox.curselection()
    listbox.delete(select)

def changebg(event):
    try:
        selectedcolor=listbox.get(listbox.curselection())
        root.config(background=selectedcolor)
    except:
        pass
frame=Frame(root,width=45,height=45)
scrollbar=Scrollbar(frame)
listbox=Listbox(frame,yscrollcommand=scrollbar.set)
add_box=Entry(root)
add_button=Button(root,text="Add",command=addcolor)
delete_button=Button(root,text="Delete",command=remove)

colors=["red","blue","yellow","green","purple"]
for c in colors:
    listbox.insert(END,c)
listbox.bind("<<ListboxSelect>>",changebg)
frame.pack(anchor=CENTER)
scrollbar.pack(anchor=CENTER,side=RIGHT,fill=Y)
listbox.pack(anchor=CENTER,side=RIGHT)
scrollbar.config(command=listbox.yview)
add_box.pack(anchor=S)
add_button.pack(anchor=S)
delete_button.pack(anchor=S)
root.mainloop()