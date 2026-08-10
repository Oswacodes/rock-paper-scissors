import tkinter as tk
import random

def play_game():
    player= choice.get().lower()
    computer = random.choice(["rock","paper","scissors"])
    if player not in ["rock","paper","scissors"]:
        result.config(text="please enter rock ,paper , or scissors.")
        return
    if player == computer:
            message = "it's a tie!"
    elif player == "rock" and computer == "scissors":
        message == "you win!"
    elif player == "paper" and computer == "rock":
        message == "you win!"
    elif player == "scissors" and computer == "paper":
        message == "you win!"
    else:
        message = "computer wins!"

    result.config(
            text=f"you:{player}\nComputer:{computer}\n{message}"
        )
        
window = tk.Tk()
window.title("rock paper scissors")
window.geometry("500x400")
window.configure(bg="lightblue")

title = tk.Label(window , text="rock paper scissors" , bg="lightblue")
title.pack(pady=30)
instruction = tk.Label(window, text="chose rock , paper , or scissors",bg="lightblue")
instruction.pack()

choice = tk.Entry(window)
choice.pack(pady=10)

button = tk.Button(window,text="play" , command=play_game)
button.pack(pady=10)

result=tk.Label(window, text="", bg="lightblue")
result.pack(pady=10)

window.mainloop()
