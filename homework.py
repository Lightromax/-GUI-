from tkinter import *

root=Tk()
root.geometry("100x100")

North=Button(root,text="North",background="lime",command=print("You went north"),activeforeground="brown",activebackground="purple",width=12,height=3,font=("Arial",10,"bold"))
West=Button(root,text="West",background="orange",command=print("You went west"),activeforeground="purple",activebackground="brown",width=12,height=3)
South=Button(root,text="South",background="green",command=print("You went south"),activeforeground="black",activebackground="yellow",width=12,height=3)
East=Button(root,text="East",background="orange",command=print("You went east"),activeforeground="yellow",activebackground="black",width=12,height=3)

North.pack(side="top")
West.pack(side="left")
South.pack(side="bottom")
East.pack(side="right")

root.mainloop()