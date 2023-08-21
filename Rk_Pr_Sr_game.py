from random import random, randint
from tkinter import *
from tkinter import ttk
from tkinter import Tk
from PIL import Image
from PIL import ImageTk
root = Tk()
root.title("Rock Paper scissor")
root.configure(bg="#FFAD00")
root.resizable()

msg = Label(root, text=" ", font=("bold", 20), bg="#FFAD00")
msg.grid(row=5, column=2)
def update_msg(x):
    msg["text"] = x

def update_image(x):
    choices = ["rock", "paper", "scissor"]
    comp_choice = choices[randint(0, 2)]
    if comp_choice == "rock":
        comp_label.configure(image=rock_comp)
    elif comp_choice == "paper":
        comp_label.configure(image=paper_comp)
    else:
        comp_label.configure(image=scissor_comp)

    if x == "rock":
        user_label.configure(image=rock_user)
    elif x == "paper":
        user_label.configure(image=paper_user)
    else:
        user_label.configure(image=scissor_user)
    check_win(x, comp_choice)

# INSERT pictures
rock_user = ImageTk.PhotoImage(Image.open("rock_user.png"))
rock_comp = ImageTk.PhotoImage(Image.open("rock_comp.png"))
paper_comp = ImageTk.PhotoImage(Image.open("paper_comp.png"))
paper_user = ImageTk.PhotoImage(Image.open("paper_user.png"))
scissor_user = ImageTk.PhotoImage(Image.open("scissor_user.png"))
scissor_comp = ImageTk.PhotoImage(Image.open("scissor_comp.png"))

comp_label = Label(root, image=rock_comp, bg="#FFAD00")
comp_label.grid(row=1, column=0)
user_label = Label(root, image=rock_user, bg="#FFAD00")
user_label.grid(row=1, column=5)

# label for computer and user

comp_side = Label(root, font=60,  text="computer", bg="#FFAD00")
comp_side.grid(row=0, column=1)
user_side = Label(root, font=60,  text="You", bg="#FFAD00")
user_side.grid(row=0, column=4)

# score label

comp_score = Label(root, text="0", bg="#FFAD00")
comp_score.grid(row=1, column=1)
user_score = Label(root, text="0", bg="#FFAD00")
user_score.grid(row=1, column=4)

def comps_score():
    score = int(comp_score["text"])
    score = score+1
    comp_score["text"] = str(score)
def users_score():
    score1 = int(user_score["text"])
    score1 = score1+1
    user_score["text"] = str(score1)

# add buttons
global rock, paper, scissor
rock = Button(root, text="ROCK", width=20, height=2, bg="#FF3E4D", command=lambda: update_image("rock"))
rock.grid(row=3, column=1)
paper = Button(root, text="PAPER",  width=20, height=2, bg="#FAD02E", command=lambda: update_image("paper"))
paper.grid(row=3, column=2)
scissor = Button(root, text="SCISSOR",  width=20, height=2, bg="#0ABDE3", command=lambda: update_image("scissor"))
scissor.grid(row=3, column=3)

def check_win(you, comp):
    if comp ==you:
        update_msg("its a tie!!")
    elif you == "rock":
        if comp == "paper":
            update_msg(" you loose!!")
            comps_score()
        else:
            update_msg("you win!!")
            users_score()
    elif you == "paper":
        if comp == "rock":
            update_msg("You win!!")
            users_score()
        else:
            update_msg("you loose!!")
            comps_score()
    elif you == "scissor":
        if comp == "paper":
            update_msg("you win!!")
            users_score()
        else:
            update_msg("you loose!!")
            comps_score()
    else:
        pass



root.mainloop()
