from tkinter import *
from tkinter.ttk import *
#strftime is a method used to format date and time objects into readable strings
from time import strftime

root=Tk()
root.config(background="blue")
root.geometry("350x70")
root.title("Clock")
Time=Label(root,background="blue",font=("Mistral",40,"bold"))
Time.pack(anchor="center")

def showtime():
    s=strftime('%H:%M:%S %p')
    Time.config(text=s)
    Time.after(1000,showtime)

showtime()
root.mainloop()