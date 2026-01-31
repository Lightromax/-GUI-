from tkinter import *
from tkinter.font import BOLD
from tkinter.ttk import *
from gtts import gTTS
from playsound import playsound
import pygame
import os
import time
#gtts is Google Text To Speech library

root=Tk()
root.config(background="lightblue")
root.geometry("300x300")

def play1():
    language=lang_combo.get()
    #f1=input("Enter the file name")
    a1=gTTS(text=text_box.get(),lang=language,slow=False)
    a1.save("convert.mp3")
    
    playsound("convert.mp3")

    os.remove("convert.mp3")

langVal=["fr","en","es","de"]
Title_label=Label(root,text="Text to Speech",background="lightblue",font=("Ariel",18,BOLD))
text_box=Entry(root)
text_button=Button(root,text="Speak",command=play1)
lang_combo=Combobox(root,values=langVal,)

Title_label.pack(anchor="n")
text_button.pack(anchor="center",side=BOTTOM)
text_box.pack(anchor="center",side=BOTTOM)
lang_combo.pack(anchor="center",side=TOP)

root.mainloop()