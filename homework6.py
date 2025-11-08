import random
from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.geometry("350x140")
root.title("Clock n Day")

Day = Label(root, font=("Arial", 40, "bold"))
Time = Label(root, font=("Mistral", 40, "bold"))
Time.pack(anchor="center")
Day.pack(anchor="n")

def random_rgb_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f'#{r:02x}{g:02x}{b:02x}'

def showtime():
    d = strftime('%d %b, %Y')
    s = strftime('%H:%M:%S %p')
    color = random_rgb_color()

    root.config(background=color)
    Day.config(text=d, background=color)
    Time.config(text=s, background=color)

    root.after(1000, showtime)

showtime()
root.mainloop()