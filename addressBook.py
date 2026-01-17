from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from tkinter.filedialog import *

root=Tk()
root.geometry("800x700")
root.title("Address Book")

address_book={}

def clearall():
    name_box.delete(0,END)
    address_box.delete(0,END)
    age_box.delete(0,END)
    email_box.delete(0,END)
    phone_numberbox.delete(0,END)
def update():
    key=name_box.get()
    if key == "":
        messagebox.showinfo("Error","Name Cannot be empty")
    else:
        if key not in address_book.keys():
            list_box.insert(END,key)
        address_book[key]=(address_box.get(),age_box.get(),email_box.get(),phone_numberbox.get())
        clearall()
#adds to listbox only if it is a new entry
#.keys func gives us all the keys of the dictionary
def edit():
    clearall()
    index=list_box.curselection()
    if index:
        name_box.insert(0,list_box.get(index))
        details=address_book[name_box.get()]
        address_box.insert(0,details[0])
        age_box.insert(0,details[1])
        email_box.insert(0,details[2])
        phone_numberbox.insert(0,details[3])
        
    else:
        messagebox.showinfo("Error2","No selection made")
def delete():
    index=list_box.curselection()
    if index:
        del address_book[list_box.get(index)]
        list_box.delete(index)
        clearall()
    else:
        messagebox.showinfo("Error2","No selection made")
def display(event):
    newWindow=Toplevel(root)
    index=list_box.curselection()
    contact=""
    if index:
        key=list_box.get(index)
        contact="Name  :  "+key+"\n\n"
        details=address_book[key]
        contact += "Address : "+details[0]+"\n"
        contact += "Age     : "+details[1]+"\n"
        contact += "Email   : "+details[2]+"\n"
        contact += "PhoneNumber:"+details[3]+"\n"
    lbl=Label(newWindow)
    lbl.grid(row=0,column=0)
    lbl.config(text=contact)
def reset():
    clearall()
    list_box.delete(0,END)
    address_book.clear()
def save():
    output=asksaveasfile(defaultextension=".txt")
    if output:
        print(address_book,file=output)
        reset()
    else:
        messagebox.showinfo("Error3","Address book not saved")
def open():
    global address_book
    reset()
    inputOpen=askopenfile(title="Open File")
    if inputOpen:
        #eval executes string as a python expression
        address_book=eval(inputOpen.read())
        for key in address_book.keys():
            list_box.insert(END,key)
        myaddressbook.config(text=os.path.basename(inputOpen.name))
    else:
        messagebox.showinfo("Error3","No address book available")

name_Label=Label(root,text="Name:")
address_Label=Label(root,text="Address:")
age_Label=Label(root,text="Age:")
email_Label=Label(root,text="Email:")
name_box=Entry(root)
phone_numberlabel=Label(root,text="Phone Number:")
myaddressbook=Label(root)
address_box=Entry(root)
phone_numberbox=Entry(root)
age_box=Entry(root)
email_box=Entry(root)
list_box=Listbox(root,width=50,height=19)
add_button=Button(root,text="Update/Add",width=23,command=update)
delete_button=Button(root,text="Delete",width=23,command=delete)
save_button=Button(root,text="Save",width=23,command=save)
edit_button=Button(root,text="Edit",width=23,command=edit)
open_button=Button(root,text="Open",width=23,command=open)
list_box.bind("<<ListboxSelect>>",display)


name_Label.place(x=500,y=100)
address_Label.place(x=500,y=200)
age_Label.place(x=500,y=300)
email_Label.place(x=500,y=400)
phone_numberlabel.place(x=500,y=500)
phone_numberbox.place(x=600,y=500)
myaddressbook.place(x=400,y=700)
name_box.place(x=550,y=100)
address_box.place(x=550,y=200)
age_box.place(x=550,y=300)
email_box.place(x=550,y=400)
list_box.place(x=100,y=50)
open_button.place(x=650,y=10)
save_button.place(x=100,y=10)
edit_button.place(x=100,y=360)
delete_button.place(x=100,y=390)
add_button.place(x=500,y=600)
root.mainloop()