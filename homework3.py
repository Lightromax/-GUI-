from tkinter import *

root=Tk()
root.geometry("450x450")
root.config(background="black")
root.title("Pounds to Dollars")

def convert():
    pound=input_box.get()
    dollars=(float(pound)+0.34)
    output_label.config(text="Pounds in Dollars:$"+str(dollars))

Title_Label=Label(root,text="Pounds to dollars",background="grey")
input_label=Label(root,text="Pounds")
input_box=Entry(root)
output_label=Label(root,text="Pounds in Dollar",background="grey")
convert_button=Button(root,text="Convert",activebackground="blue",activeforeground="purple",command=convert,background="lightblue")
Title_Label.place(x=200,y=100)
input_label.place(x=100,y=200)
input_box.place(x=300,y=200)
output_label.place(x=200,y=300)
convert_button.place(x=200,y=400)

root.mainloop()