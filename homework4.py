from tkinter import *

root=Tk()
root.geometry("700x300")
root.config(background="green")
root.title("Time and speed converted to distance")

def distance():
    time=timeinput_box.get()
    speed=speedinput_box.get()
    distance=(float(time)*float(speed))
    output_label.config(text="Time and speed converted to distance:"+str(distance)+"km")

Title_Label=Label(root,text="Time and speed distance to distance",background="green")
input_label=Label(root,text="TxS = distance-time in first box, speed in last")
timeinput_box=Entry(root)
speedinput_box=Entry(root)
output_label=Label(root,text="Time and speed distanceed to distance",background="green")
distance=Button(root,text="distance",activebackground="blue",activeforeground="lightblue",command=distance,background="lightblue")
speed_label=Label(root,text="speed-measuring in km-",bg="green")
time_label=Label(root,text="time-in hrs-",bg="green")
speed_label.grid(row=8,column=6)
time_label.grid(row=7,column=6)
Title_Label.grid(row=1,column=5)
input_label.grid(row=7,column=1)
timeinput_box.grid(row=7,column=7)
speedinput_box.grid(row=8,column=7)
output_label.grid(row=9,column=5)
distance.grid(row=10,column=5)

root.mainloop()