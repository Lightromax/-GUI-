from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *

root=Tk()
root.geometry("500x500")
root.title("Student Grading System")

def calculate():
    n1=int(math_box.get())
    n2=int(english_box.get())
    n3=int(science_box.get())
    plused=n1+n2+n3
    div=plused/60
    fans=div*100
    print(fans)

def save():
    name=name_box.get()
    if name:
        listbox.insert(name,END)
    else:
        showinfo("Error","Name cannot be empty")

Title_label=Label(root,text="Student Grading System",font=("Ariel",18))
name_label=Label(root,text="Name:",font=("Ariel",10))
name_box=Entry(root)
roll_label=Label(root,text="Roll no:",font=("Ariel",10))
roll_box=Entry(root)
math_label=Label(root,text="Math Marks(out of 20):",font=("Ariel",10))
math_box=Entry(root)
science_label=Label(root,text="Science Marks(out of 20):",font=("Ariel",10))
science_box=Entry(root)
english_label=Label(root,text="English Marks(out of 20):",font=("Ariel",10))
english_box=Entry(root)
cal_button=Button(root,text="Calculate Grade",command=calculate)
save_button=Button(root,text="Save Grade",command=save)
listbox=Listbox(root,width=30)

Title_label.place(x=10,y=10)
name_label.place(x=20,y=50)
name_box.place(x=170,y=50)
roll_label.place(x=20,y=70)
roll_box.place(x=170,y=70)
math_label.place(x=20,y=90)
math_box.place(x=170,y=90)
science_label.place(x=20,y=110)
science_box.place(x=170,y=110)
english_label.place(x=20,y=130)
english_box.place(x=170,y=130)
cal_button.place(x=50,y=160)
save_button.place(x=57,y=190)
listbox.place(x=10,y=240)

root.mainloop()