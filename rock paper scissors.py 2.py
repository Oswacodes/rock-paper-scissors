import tkinter as tk
import random

def play():
    player= choice_entry.get().lower()
    computer = random.choice(["rock","paper","scissors"])
    
    if player not in ["rock","paper","scissors"]:
        result.config(text="please enter rock ,paper , or scissors.")
        return
    
    if player == computer:
            message = "it's a tie!"
    elif player == "rock" and computer == "scissors":
        message = "you win!"
    elif player == "paper" and computer == "rock":
        message =" you win!"
    elif player == "scissors" and computer == "paper":
        message = "you win!"
    else:
        message = "computer wins!"

    result.config(text="you:" + player +" - Computer: " + computer + "- " + message)
        
    
def reset ():
    choice_entry.delete(0,tk.END)
    result.config(text="")

def exit_game():
    window.destroy()

window = tk.Tk()
window.title("rock paper scissors")
window.geometry("500x400")
window.configure(bg="lightblue")

title=tk.Label(
    window,
    text="rock paper scissors",
    font=("Ariel",24, "bold"),
    bg="lightblue"
)
title.pack(pady=30)


instruction=tk.Label(window,text="chose rock , paper or scissors:",font=("Ariel",14 ),bg="lightblue")
instruction.pack(pady=10)

choice_entry=tk.Entry( window, font=("Ariel",14))
choice_entry.pack(pady=10)

play_button=tk.Button(window,text="play",font=("Ariel",14),command=play)
play_button.pack(pady=10)

reset_button=tk.Button(window,text="reset", font=("Ariel",14), command=reset)
reset_button.pack(pady=5)

exit_button=tk.Button( window,text="Exit",font=("Ariel",14),command=exit_game)

exit_button.pack(pady=5)

result=tk.Label(window, text="",font=("Ariel",14),bg="lightblue")
result.pack(pady=10)

window.mainloop()
