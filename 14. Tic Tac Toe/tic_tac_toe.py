from tkinter import *  # noqa: F403
import tkinter.messagebox as msg

# Initialize the main window
root = Tk()
root.title("TIC-TAC-TOE - By Aya Nabil")
root.configure(bg="#2E3440")  # Set a dark theme background

# Global variables
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # Available positions on the board
mark = ""  # Current player's mark (X or O)
count = 0  # Count of moves made
panels = [" " for _ in range(10)]  # Represents the game board (index 0 unused)


# Function to check if a player has won
def win(panels, sign):
    return (
        (panels[1] == panels[2] == panels[3] == sign)  # Top row
        or (panels[4] == panels[5] == panels[6] == sign)  # Middle row
        or (panels[7] == panels[8] == panels[9] == sign)  # Bottom row
        or (panels[1] == panels[4] == panels[7] == sign)  # Left column
        or (panels[2] == panels[5] == panels[8] == sign)  # Middle column
        or (panels[3] == panels[6] == panels[9] == sign)  # Right column
        or (panels[1] == panels[5] == panels[9] == sign)  # Diagonal
        or (panels[3] == panels[5] == panels[7] == sign)
    )  # Diagonal


# Function to handle button clicks
def checker(digit):
    global count, mark, digits

    if digit in digits:
        digits.remove(digit)  # Remove the position from available positions

        # Determine the current player's mark (X or O)
        if count % 2 == 0:
            mark = "X"
        else:
            mark = "O"

        panels[digit] = mark  # Update the game board
        buttons[digit].config(text=mark)  # Update the button text
        count += 1  # Increment the move count

        # Check if the current player has won
        if win(panels, mark):
            msg.showinfo("Result", f"Player {mark} wins!")
            root.destroy()
        # Check if the game is a tie
        elif count > 8:
            msg.showinfo("Result", "Match Tied!")
            root.destroy()


# Function to reset the game
def reset_game():
    global digits, mark, count, panels
    digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    mark = ""
    count = 0
    panels = [" " for _ in range(10)]
    for button in buttons.values():
        button.config(text=" ")


# Create buttons for the game board
buttons = {}
for i in range(1, 10):
    button = Button(
        root,
        text=" ",
        font=("Arial", 20),
        width=6,
        height=3,
        bg="#4C566A",
        fg="#D8DEE9",
        command=lambda i=i: checker(i),
    )
    button.grid(row=(i - 1) // 3 + 1, column=(i - 1) % 3, padx=5, pady=5)
    buttons[i] = button

# Add labels for players
Label(root, text="Player 1: X", font=("Arial", 15), bg="#2E3440", fg="#D8DEE9").grid(
    row=0, column=0
)
Label(root, text="Player 2: O", font=("Arial", 15), bg="#2E3440", fg="#D8DEE9").grid(
    row=0, column=2
)

# Add a reset button
reset_button = Button(
    root,
    text="Reset",
    font=("Arial", 15),
    bg="#BF616A",
    fg="#D8DEE9",
    command=reset_game,
)
reset_button.grid(row=4, column=0, columnspan=3, sticky=N + E + W + S, padx=5, pady=5)

# Start the main loop
root.mainloop()
