from tkinter import *
from tkinter.messagebox import *
from time import *

root=Tk()
root.geometry("600x300")
###############################################
#define
def start():
    start_button.config(state="disabled")
    Hour_box.config(state="disabled")
    Minute_box.config(state="disabled")
    second_box.config(state="disabled")
    try:
        temp= int(Hour_box.get())*3600 + int(Minute_box.get())*60 + int(second_box.get())
    except:
        print("Please enter the right value for time")
    while(temp > -1):
        mins,secs= divmod(temp,60) #mins = temp//60 secs=temp%60
        hours=00
        if mins > 60:
            hours,mins=divmod(mins,60)
        hour.set("{00:2d}".format(hours))
        minute.set("{00:2d}".format(mins))
        second.set("{00:2d}".format(secs))
        root.update()
        sleep(1)
        if temp == 00:
            showinfo("countdown","TIMES UPPP!!!!!!!")
        temp -= 1
###############################################
#variables
hour=StringVar()
minute=StringVar()
second=StringVar()
#variables-setting default value as zero
hour.set("00")
minute.set("00")
second.set("00")
###############################################
#Creating
Hour_box=Entry(root,width=11,textvariable=hour,font=("Ariel",18,""))
Minute_box=Entry(root,width=11,textvariable=minute,font=("Ariel",18,""))
second_box=Entry(root,width=11,textvariable=second,font=("Ariel",18,""))
start_button=Button(root,text="Start Timer",command=start)
###############################################
#Placing
Hour_box.place(x=200,y=100)
Minute_box.place(x=300,y=100)
second_box.place(x=400,y=100)
start_button.place(x=300,y=200)

root.mainloop()