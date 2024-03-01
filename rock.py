from tkinter import *
import random
rps = Tk()
rps.geometry("300x300")
rps.titel("Rock-Paper-Scissor | @Coerres")

user_score = 0
comp_score = 0
user_choice = ""
comp_choice = ""

def choice_to_number(choice):
    rps = {'rock':0, 'paper':1, 'scissor':2}
def number_to_choice(number):
    rps = {0: 'rock', 1: 'paper', 2: 'scissor'}

def random_computer_choice():
    return random.choice(['rock', 'paper', 'scissor'])


def rock():
    global user_choice
    global comp_choice
    user_choice = "rock"
    comp_choice = random_computer_choice()
    result(user_choice, comp_choice)

def paper():
    global user_choice
    global comp_choice
    user_choice = "rock"
    comp_choice = random_computer_choice()
    result(user_choice, comp_choice)

def scissor():
    global user_choice
    global comp_choice
    user_choice = "rock"
    comp_choice = random_computer_choice()
    result(user_choice, comp_choice)

#Create label and buttons
button_rock = Button(text="      ROCK      ", bg = "#808487",font = ("arial",15,"italic bold"), relief = RIDGE,
                    activebackground = "#059458", activeforeground = "white", width = 24)
button_rock.grid(column = 0, row = 1)
button_paper = Button(text="      PAPER      ", bg = "#808487",font = ("arial",15,"italic bold"), relief = RIDGE,
                    activebackground = "#059458", activeforeground = "white", width = 24)
button_rock.grid(column = 0, row = 2)
button_scissor = Button(text="      SCISSOR      ", bg = "#808487",font = ("arial",15,"italic bold"), relief = RIDGE,
                    activebackground = "#059458", activeforeground = "white", width = 24)
button_rock.grid(column = 0, row = 3)


rps.mainloop()