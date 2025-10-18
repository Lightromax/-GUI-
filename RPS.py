from tkinter import *
import random

root=Tk()
root.config(background="lightblue")
root.title="Rock Paper Scissors"
root.geometry("700x500")

playerScore=0
computerScore=0
options=[("rock",0),("paper",1),("scissors",2)]

def computer_wins():
    global playerScore, computerScore
    computerScore += 1
    Action_label.config(text="Computer Won!!")
    CompScored_Label.config(text="Computer Scored" +str(computerScore))
    PLayerScored_label.config(text="Player scored" +str(playerScore))
    
def player_wins():
    global playerScore, computerScore
    playerScore += 1
    Action_label.config(text="Player won")
    CompScored_Label.config(text="Computer Scored" +str(computerScore))
    PLayerScored_label.config(text="Player scored" +str(playerScore))

Title_label=Label(root,text="Rock, Paper, Scissors")
Title_label.grid(row=1,column=5)
Action_label=Label(root)
Action_label.grid(row=3,column=5)
Options_label=Label(root,text="Your Options:")
Options_label.grid(row=4, column=1)
PlayerSelection_Label=Label(root,text="Your selection")
PlayerSelection_Label.grid(row=13,column=2)
ComputerSelection_Label=Label(root,text="Computer's selection")
ComputerSelection_Label.grid(row=12,column=2)
PLayerScored_label=Label(root,text="You Scored")
PLayerScored_label.grid(row=13,column=6)
CompScored_Label=Label(root,text="Computer scored")
CompScored_Label.grid(row=12,column=6)
Rock_button=Button(root,text="Rock",width=10)
Rock_button.grid(row=4,column=2)
Paper_button=Button(root,text="Paper",width=10)
Paper_button.grid(row=4,column=5)
Scissors_button=Button(root,text="Scissors",width=10)
Scissors_button.grid(row=4,column=7)

root.mainloop()