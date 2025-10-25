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

def draw():
    global playerScore, computerScore
    Action_label.config(text="!!!Draw!!!")
    CompScored_Label.config(text="Computer Scored" +str(computerScore))
    PLayerScored_label.config(text="Player scored" +str(playerScore))
    
def getcomputer_choice():
    return random.choice(options)
    
def plyr_sel(player_input):
    global playerScore, computerScore
    print(player_input)
    computer_input=getcomputer_choice()
    print(computer_input)
    PlayerSelection_Label.config(text="You selected "+str(player_input[0]))
    ComputerSelection_Label.config(text="Computer selected "+str(computer_input[0]))
    if player_input == computer_input:
        draw()
    if player_input [1] == 0:
        if computer_input [1] == 1:
            computer_wins()
        elif computer_input [1] == 2:
            player_wins()
    if player_input [1] == 1:
        if computer_input [1] == 2:
            computer_wins()
        elif computer_input [1] == 0:
            player_wins()
    if player_input [1] == 2:
        if computer_input [1] == 0:
            computer_wins()
        elif computer_input [1] == 1:
            player_wins()

Title_label=Label(root,text="Rock, Paper, Scissors")
Title_label.grid(row=1,column=5)
Action_label=Label(root)
Action_label.grid(row=3,column=5)
Options_label=Label(root,text="Your Options:")
Options_label.grid(row=4, column=1)
PlayerSelection_Label=Label(root,text="You selected")
PlayerSelection_Label.grid(row=13,column=2)
ComputerSelection_Label=Label(root,text="Computer selected")
ComputerSelection_Label.grid(row=12,column=2)
PLayerScored_label=Label(root,text="You Scored")
PLayerScored_label.grid(row=13,column=6)
CompScored_Label=Label(root,text="Computer scored")
CompScored_Label.grid(row=12,column=6)
Rock_button=Button(root,text="Rock",width=10,command=lambda:plyr_sel(options[0]))
Rock_button.grid(row=4,column=2)
Paper_button=Button(root,text="Paper",width=10,command=lambda:plyr_sel(options[1]))
Paper_button.grid(row=4,column=5)
Scissors_button=Button(root,text="Scissors",width=10,command=lambda:plyr_sel(options[2]))
Scissors_button.grid(row=4,column=7)

root.mainloop()
print("Your score"+str(playerScore))
print("Computer's score: "+str(computerScore))
if computerScore >= playerScore:
    print("Computer wins")
else:
    print("Player wins")