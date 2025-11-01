from tkinter import *

root=Tk()
root.config(background="grey")
root.title("guess the number")
root.geometry("300x300")

Title_label=Label(root,text="welcome to our game",background="grey")
Namequestion_label=Label(root,text="what is your name?",background="grey")
Name_box=Entry(root)
Enter_button=Button(root,text="Enter",background="grey")
Guess_label=Label(root,text="have a guess:",background="grey")
Guess_box=Entry(root)
Guess_button=Button(root,text="Guess")

Title_label.grid(row=1,column=1)
Namequestion_label.grid(row=2,column=1)
Name_box.grid(row=3,column=1)
Enter_button.grid(row=3,column=2)
Guess_label.grid(row=4,column=1)
Guess_box.grid(row=4,column=2)
Guess_button.grid(row=4,column=3)

root.mainloop()