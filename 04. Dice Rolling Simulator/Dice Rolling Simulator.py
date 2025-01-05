import tkinter as tk
from PIL import Image, ImageTk
import random

# Initialize the main window
root = tk.Tk()
root.geometry("500x500")  # Slightly larger window for better UI
root.title("Python Dice Roller - Beginner Project")
root.configure(bg="#FFD700")  # Set a colorful background (golden yellow)


# Function to update the dice image when the button is clicked
def roll_dice():
    # Randomly select a dice image
    dice_image_path = random.choice(dice_images)
    dice_image = ImageTk.PhotoImage(Image.open(dice_image_path))

    # Update the image in the label
    dice_label.configure(image=dice_image)
    dice_label.image = dice_image  # Keep a reference to avoid garbage collection

    # Update the status label to show the result
    dice_number = dice_image_path.split(".")[0][
        -1
    ]  # Extract the dice number from the filename
    status_label.config(
        text=f"You rolled a {dice_number}!",
        fg="dark blue",
        font=("Helvetica", 14, "bold"),
    )


# List of dice image file paths
dice_images = ["die1.png", "die2.png", "die3.png", "die4.png", "die5.png", "die6.png"]

# Load the initial dice image
initial_image = ImageTk.PhotoImage(Image.open(random.choice(dice_images)))

# Create a label to display the dice image
dice_label = tk.Label(root, image=initial_image, bg="#FFD700")
dice_label.pack(pady=20)  # Add some padding

# Create a label to display the status (result of the roll)
status_label = tk.Label(
    root,
    text="Click 'Roll the Dice' to start!",
    fg="dark green",
    bg="#FFD700",
    font=("Helvetica", 12, "italic"),
)
status_label.pack(pady=10)

# Create a button to roll the dice
roll_button = tk.Button(
    root,
    text="Roll the Dice",
    fg="white",
    bg="dark green",
    font=("Helvetica", 14, "bold"),
    command=roll_dice,
    relief="raised",  # Button style
    padx=10,  # Horizontal padding
    pady=5,  # Vertical padding
)
roll_button.pack(pady=20)

# Add a footer label for attribution or instructions
footer_label = tk.Label(
    root,
    text="A Python Beginner Project by Your Name",
    fg="gray",
    bg="#FFD700",
    font=("Helvetica", 10, "italic"),
)
footer_label.pack(side="bottom", pady=10)

# Start the main event loop to keep the window open
root.mainloop()
