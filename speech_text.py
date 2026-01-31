from tkinter import *
from tkinter.font import BOLD
from tkinter.ttk import *
import speech_recognition as sr
from tkinter import messagebox
from tkinter.filedialog import *

root = Tk()
root.geometry("400x300")
root.config(background="lightblue")

def stt():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("say anything")
        audio=r.listen(source)
        try:
            t=r.recognize_google(audio)
        except:
            t="sry could not reognize your voice"
        text_widget.delete(1.0,END)
        text_widget.insert(END,t)
def save():
    fout=asksaveasfile(defaultextension=".txt")
    if fout:
        print(text_widget.get(1.0,END),file=fout)
    else:
        messagebox.showinfo("No text to save")


Title_label=Label(root,text="Speech to Text",background="lightblue",font=("Ariel",18,BOLD))
record_button=Button(root,text="Click to start recording",command=stt)
text_widget=Text(root,width=13,height=13)
save_button=Button(root,text="Save Text",command=save)

Title_label.pack(anchor="n")
record_button.pack(anchor="n",side=BOTTOM)
text_widget.pack(anchor="center")
save_button.pack(anchor="s",side=BOTTOM)

root.mainloop()