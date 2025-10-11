from tkinter import *

root=Tk()
root.geometry("450x450")
root.config(background="grey")
root.title("Celsius to Fahrenheit")

def convert():
    celsius_temp=input_box.get()
    fahrenheit_convertion=(float(celsius_temp)*9/5)+ 32
    output_label.config(text="Temperature in Fahrenheit:"+str(fahrenheit_convertion))

Title_Label=Label(root,text="Celsius to Fahrenheit",background="grey")
input_label=Label(root,text="Temperature in Degrees Celsius")
input_box=Entry(root)
output_label=Label(root,text="Temperature in Fahrenheit",background="grey")
convert_button=Button(root,text="Convert",activebackground="green",activeforeground="lime",command=convert,background="lightblue")
Title_Label.place(x=200,y=100)
input_label.place(x=100,y=200)
input_box.place(x=300,y=200)
output_label.place(x=200,y=300)
convert_button.place(x=200,y=400)

root.mainloop()