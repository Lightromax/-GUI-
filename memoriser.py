from tkinter import *
from tkinter.ttk import *

root=Tk()
root.title("Memoriser")
root.geometry("500x400")
#######################################
#create
save_button=Button(root,text="Save")
add_button=Button(root,text="Add")
open_button=Button(root,text="Open")
delete_button=Button(root,text="Delete")
name_box=Entry(root)
#list_box=
#######################################
#placing
save_button.pack(anchor="n")
open_button.pack(anchor="w")
delete_button.pack(anchor="e")
name_box.pack(anchor="s")
add_button.pack(anchor="s")

root.mainloop()