from tkinter import *
from tkinter.ttk import *

root=Tk()
root.title("Food Categories")

def showchoice():
    choices=category.get()
    

categories=["Fruits","Vegetables","Drinks"]
category=Combobox(root,values=categories)
choice=StringVar()
fruit1=Radiobutton(root,text="Apple",variable=choice,value="A")
fruit2=Radiobutton(root,text="Banana",variable=choice,value="B")
veg1=Radiobutton(root,text="Carrot",variable=choice,value="CA")
veg2=Radiobutton(root,text="Onion",variable=choice,value="O")
drink1=Radiobutton(root,text="Coffee",variable=choice,value="CO")
drink2=Radiobutton(root,text="Tea",variable=choice,value="T")

category.grid(row=1,column=5)
fruit1.grid(row=2,column=5)
fruit2.grid(row=3,column=5)
veg1.grid(row=2,column=6)
veg2.grid(row=3,column=6)
drink1.grid(row=2,column=7)
drink2.grid(row=3,column=7)

root.mainloop()