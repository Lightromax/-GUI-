from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import *

root=Tk()
root.title("Memoriser")
root.geometry("500x400")
#######################################
#Function to add item to list box
def additem():
    list_box.insert(END,name_box.get())
    name_box.delete(0,END)
def delete():
    index=list_box.curselection()
    if index:
        list_box.delete(index)
def open():
    inputOpen=askopenfile(title="open file")
    if inputOpen is not None:
        list_box.delete(0,END)
        items=inputOpen.readlines()
        for item in items:
            list_box.insert(END,item.strip())
def save():
    ouput=asksaveasfile(defaultextension=".txt")
    if ouput is not None:
        for item in list_box.get(0,END):
            print(item.strip(),file=ouput)
        list_box.delete(0,END)
#######################################
#create
save_button=Button(root,text="Save",command=save)
add_button=Button(root,text="Add",command=additem)
open_button=Button(root,text="Open",command=open)
delete_button=Button(root,text="Delete",command=delete)
name_box=Entry(root)
frame=Frame(root)
scrollbar=Scrollbar(frame,orient="vertical")
list_box=Listbox(frame,width=50,yscrollcommand=scrollbar.set,background="blue")
for i in range(1,101):
    list_box.insert(END,"list"+str(i))
#######################################
#placing
save_button.pack(anchor="n",side=TOP)
open_button.pack(anchor="n",side=TOP)
name_box.pack(anchor="n")
delete_button.pack(anchor="n",side=LEFT)
add_button.pack(anchor="n",side=RIGHT)
frame.pack(side=RIGHT)
scrollbar.pack(side=RIGHT,fill=Y)

list_box.pack(side=RIGHT)
scrollbar.config(command=list_box.yview)

root.mainloop()