from tkinter import *
#creating window
root=Tk()
root.geometry("100x100")
#creating a button
Play=Button(root,text="Play",background="lime",command=root.destroy)

Play.pack(side="top")


root.mainloop()
print("Successfully terminted ;] BEEB BOB BEEB BOB")