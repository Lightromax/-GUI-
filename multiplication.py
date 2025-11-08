from tkinter import *
from tkinter.ttk import *

root=Tk()
root.title("Multiplication Table")
root.geometry("330x220")

def resulting():
    res=""
    for i in range(rangevalue.get()+1):
        res+=str(num.get())+" x "+str(i)+" = "+str(num.get()*i)+"\n"
    result.config(text=res)

Title_Label=Label(root,text="Multiplication Table")
input_label=Label(root,text="Choose your number and range!!!")
#specifies we only want integer values
num=IntVar()
numbers=Combobox(root,textvariable=num,width=5)
numbers['values']=tuple (range(101))
rangevalue=IntVar()
r10=Radiobutton(root,text="10",variable=rangevalue,value=10)
r20=Radiobutton(root,text="20",variable=rangevalue,value=20)
r30=Radiobutton(root,text="30",variable=rangevalue,value=30)
result=Label(root)
generate_button=Button(root,text="Generate",command=resulting)

Title_Label.grid(row=1,column=5)
input_label.grid(row=2,column=1)
numbers.grid(row=2,column=5)
r10.grid(row=2,column=6)
r20.grid(row=3,column=6)
r30.grid(row=4,column=6)
result.grid(row=6,column=5)
generate_button.grid(row=5,column=5)

root.mainloop()