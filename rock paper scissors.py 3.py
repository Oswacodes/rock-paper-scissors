import tkinter as tk
import random

root = tk.Tk()
root.title("rock, paper , scissors")
root.geometry("400x300")

result = tk.StringVar()
result.set("Click PLAY to start!")

def play():
    choices = ["rock" , "paper" , "scissors"]
    computer = random.choice(choices)
    player = random.choice(choices)

    if player == computer:
        outcome = "it's a tie!"
    elif (player == "rock" and computer == "scissors")or\
         (player == "paper" and computer =="rock") or\
         (player == "scissors" and computer == "paper"):
        outcome = "you win!"
    else:
        outcome = "computer wins!"

    result.set("you:" + player + " - computer:" + computer + " - \n" + outcome)

def reset():
    result.set("Click PLAY to start!")

def exit():
    root.destroy()
result_entry = tk.Entry(
    root,
    textvariable=result,
    width=45,
    justify="center"
)
result_entry.pack(pady=30)

play_button = tk.Button(
    root,
    text="PLAY",
    command=play,
    width=15
)
play_button.pack(pady=5)

reset_button = tk.Button(
    root,
    text="RESET",
    command=reset,
    width=15
)
reset_button.pack(pady=5)

exit_button = tk.Button(
    root,
    text="EXIT",
    command=exit,
    width=15
)
exit_button.pack(pady=5)

root.mainloop()
