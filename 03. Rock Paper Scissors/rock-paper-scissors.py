from tkinter import *
import random

# Initialize the main window
root = Tk()
root.geometry("500x500")  # Slightly larger window for better UI
root.resizable(0, 0)  # Disable resizing
root.title("Rock, Paper, Scissors - Beginner Project")
root.config(bg="lightblue")  # More vibrant background color

# Game title
Label(
    root,
    text="Rock, Paper, Scissors",
    font="arial 25 bold",
    bg="lightblue",
    fg="darkblue",
).pack(pady=20)

# User input section
Label(
    root,
    text="Choose one: rock, paper, scissors",
    font="arial 15 bold",
    bg="lightblue",
    fg="darkgreen",
).place(x=50, y=80)

# Variable to store user's choice
user_take = StringVar()
Entry(root, font="arial 15", textvariable=user_take, bg="white", fg="black").place(
    x=120, y=130
)

# Variable to store the result of the game
Result = StringVar()


# Function to determine the computer's choice
def computer_choice():
    comp_pick = random.randint(1, 3)
    if comp_pick == 1:
        return "rock"
    elif comp_pick == 2:
        return "paper"
    else:
        return "scissors"


# Function to play the game
def play():
    user_pick = user_take.get().lower()  # Get user's choice and convert to lowercase
    comp_pick = computer_choice()  # Get computer's choice

    # Determine the result
    if user_pick == comp_pick:
        Result.set(f"It's a tie! Both chose {user_pick}.")
    elif (
        (user_pick == "rock" and comp_pick == "scissors")
        or (user_pick == "paper" and comp_pick == "rock")
        or (user_pick == "scissors" and comp_pick == "paper")
    ):
        Result.set(f"You win! Computer chose {comp_pick}.")
    elif user_pick not in ["rock", "paper", "scissors"]:
        Result.set("Invalid choice! Please choose rock, paper, or scissors.")
    else:
        Result.set(f"You lose! Computer chose {comp_pick}.")


# Function to reset the game
def reset():
    Result.set("")  # Clear the result
    user_take.set("")  # Clear the user input


# Function to exit the game
def exit_game():
    root.destroy()  # Close the application


# Display the result
Entry(
    root,
    font="arial 12 bold",
    textvariable=Result,
    bg="white",
    fg="black",
    width=40,
    state="readonly",
).place(x=50, y=250)

# Buttons for PLAY, RESET, and EXIT
Button(
    root,
    font="arial 15 bold",
    text="PLAY",
    padx=10,
    bg="green",
    fg="white",
    command=play,
).place(x=200, y=180)
Button(
    root,
    font="arial 15 bold",
    text="RESET",
    padx=10,
    bg="orange",
    fg="white",
    command=reset,
).place(x=100, y=350)
Button(
    root,
    font="arial 15 bold",
    text="EXIT",
    padx=10,
    bg="red",
    fg="white",
    command=exit_game,
).place(x=300, y=350)

# Start the main event loop
root.mainloop()
