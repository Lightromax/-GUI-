from tkinter import *

import calendar

def showcal():
    root=Tk()
    root.geometry("700x700")
    root.title("Calender")
    root.config(background="lightblue")
    fetchyr=int(yearbox.get())
    cal=calendar.calendar(fetchyr)
    cal_label=Label(root,text=cal,font="Arial 13 bold")
    cal_label.grid(row=5,column=1,padx=20)
    root.mainloop()
if __name__ == "__main__":
    root1=Tk()
    root1.title("MainScreen")
    root1.config(background="lime")
    root1.geometry("250x250")
    Label1=Label(root1,font="Arial 13 bold",text="Calendar",background="grey")
    Label1.grid(row=1,column=1)
    yearbox=Entry(root1)
    Show=Button(root1,text="Show Calendar",command=showcal, bg="red")
    yearbox.grid(row=2,column=1)
    Show.grid(row=3,column=1)
    Exit=Button(root1,text="Exit",bg="red", command=exit)
    Exit.grid(row=6,column=1)
    root1.mainloop()