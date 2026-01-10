from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import *

############################
root=Tk()
root.geometry("600x600")
############################
def add():
    age=int(age_box.get())
    if age >= 18:
        confirmed.config(text="Confirmed your application",font='Ariel')
        listbox.insert(END,name_box.get())
    else:
        confirmed.config(text="Too young to apply. You must be 18+")
def delete():
    selectedCursor=listbox.curselection()
    listbox.delete(selectedCursor)
def open():
    input=askopenfile(title="Open File")
    if input is not None:
        listbox.delete(0,END)
        items=input.readlines()
        for item in items:
            listbox.insert(END,item.strip())
def save():
    ouput=asksaveasfile(defaultextension=".txt")
    if ouput is not None:
        for item in listbox.get(0,END):
            print(item.strip(),file=ouput)
        listbox.delete(0,END)
############################
num=IntVar()
name_label=Label(root,text="Name:")
name_box=Entry(root)
age_label=Label(root,text="Age:")
age_box=Entry(root,textvariable=num)
phoneNumber_label=Label(root,text="Phone number:")
phoneNumber_box=Entry(root)
email_label=Label(root,text="Email Address:")
email_box=Entry(root)
listbox=Listbox(root,width=40)
save_button=Button(root,text="Save",command=save)
delete_button=Button(root,text="Delete",command=delete)
add_button=Button(root,text="Edit/Add",command=add)
open_button=Button(root,text="Open",command=open)
confirmed=Label(root)
############################
name_label.place(x=400,y=50)
name_box.place(x=450,y=50)
age_label.place(x=400,y=100)
age_box.place(x=450,y=100)
phoneNumber_label.place(x=350,y=150)
phoneNumber_box.place(x=450,y=150)
email_label.place(x=350,y=200)
email_box.place(x=450,y=200)
listbox.place(x=100,y=50)
save_button.place(x=180,y=10)
open_button.place(x=180,y=230)
add_button.place(x=480,y=250)
delete_button.place(x=20,y=110)
confirmed.place(x=300,y=560)

root.mainloop()