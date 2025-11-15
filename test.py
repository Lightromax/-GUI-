from tkinter import *
from PIL import Image, ImageTk

root=Tk()
root.geometry("500x500")

image=Image.open("cgaAPP.png")
image=image.resize((500,500),Image.LANCZOS)
bg=ImageTk.PhotoImage(image)
bgLabel=Label(root,image=bg)
bgLabel.place(relwidth=1,relheight=1)

root.mainloop()