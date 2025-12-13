from tkinter import *
from tkinter.ttk import *

root=Tk()
root.title("Memoriser")
root.geometry("500x400")
#######################################
#Function to add item to list box
def additem():
    list_box.insert(END,name_box.get())
    name_box.delete(0,END)
#######################################
#create
save_button=Button(root,text="Save")
add_button=Button(root,text="Add",command=additem)
open_button=Button(root,text="Open")
delete_button=Button(root,text="Delete")
name_box=Entry(root)
frame=Frame(root)
scrollbar=Scrollbar(frame,orient="vertical")
list_box=Listbox(frame,width=50,yscrollcommand=scrollbar.set,background="blue")
for i in range(1,101):
    list_box.insert(END,"list"+str(i))
#######################################
#placing
save_button.pack(anchor="n")
open_button.pack(anchor="w")
name_box.pack(anchor="s")
add_button.pack(anchor="s")
frame.pack(side=RIGHT)
scrollbar.pack(side=RIGHT,fill=Y)
delete_button.pack(side=BOTTOM)
list_box.pack(side=RIGHT)
scrollbar.config(command=list_box.yview)

root.mainloop()