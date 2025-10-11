from tkinter import *

def showProj():
    root1=Tk()
    root1.geometry("500 x 500")
    root1.title("Project")
    root1.config(background="blue")
    created=int(EnText2.get())
    entertext=Entry(root1)
    entertext.grid(row=1,column=1)
    
if __name__ == "__main__":
    root2=Tk()
    root2.title("Create Project")
    root2.config(background="blue")
    Label1=Label(root2,font="Arial",text="Enter A Template", background="green")
    Label1.grid(row=1,column=1)
    Label2=Label(root2,font="Arial",text="Project Name", background="green")
    Label2.grid(row=3,column=1)
    EnText1=Entry(root2)
    EnText1.grid(row=2,column=1)
    EnText2=Entry(root2)
    EnText2.grid(row=4,column=1)
    Button1=Button(root2,text="Create", command=showProj, bg= "orange")
    Button1.grid(row=5,column=1)
    Button2=Button(root2,text="Exit", command=exit, bg= "red")
    Button2.grid(row=6,column=1)
    root2.mainloop()