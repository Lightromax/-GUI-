from tkinter import *
from tkinter.font import BOLD
from tkinter.ttk import *
from gtts import gTTS
import pygame
import os
#gtts is Google Text To Speech library

root=Tk()
root.config(background="lightblue")
root.geometry("300x300")

def play1():
    language="en"
    f1=input("Enter the file name")
    a1=gTTS(text=text_box.get(),lang=language,slow=False)
    a1.save(f1)
    pygame.mixer.init()
    pygame.mixer.music.load(f1)
    pygame.mixer.music.play()

Title_label=Label(root,text="Text to Speech",background="lightblue",font=("Ariel",18,BOLD))
text_box=Entry(root)
text_button=Button(root,text="Speak",command=play1)

Title_label.pack(anchor="n")
text_button.pack(anchor="center",side=BOTTOM)
text_box.pack(anchor="center",side=BOTTOM)

root.mainloop()