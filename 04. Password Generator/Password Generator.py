# Import necessary libraries
from tkinter import Tk, Label, Button, Entry, Spinbox, StringVar, IntVar, BOTTOM
import random
import string
import pyperclip


# Function to generate a random password
def generate_password():
    """
    Generates a random password based on the selected length.
    The password includes uppercase letters, lowercase letters, digits, and special characters.
    """
    password = ""

    # Ensure the password has at least one character from each category
    password = (
        random.choice(string.ascii_uppercase)  # Add an uppercase letter
        + random.choice(string.ascii_lowercase)  # Add a lowercase letter
        + random.choice(string.digits)  # Add a digit
        + random.choice(string.punctuation)  # Add a special character
    )

    # Fill the rest of the password with random characters
    for _ in range(pass_len.get() - 4):
        password += random.choice(
            string.ascii_uppercase
            + string.ascii_lowercase
            + string.digits
            + string.punctuation
        )

    # Set the generated password to the StringVar
    pass_str.set(password)


# Function to copy the password to the clipboard
def copy_password():
    """
    Copies the generated password to the clipboard using the pyperclip library.
    """
    pyperclip.copy(pass_str.get())


# Initialize the main application window
root = Tk()
root.geometry("400x400")  # Set window size
root.resizable(0, 0)  # Disable resizing
root.title("Password Generator")  # Set window title
root.configure(bg="#f0f0f0")  # Set background color

# Add a title label
Label(
    root,
    text="PASSWORD GENERATOR",
    font="arial 15 bold",
    bg="#f0f0f0",
    fg="#333333",
).pack(pady=10)

# Add a label for the password length
Label(
    root,
    text="Select Password Length:",
    font="arial 10 bold",
    bg="#f0f0f0",
    fg="#555555",
).pack(pady=5)

# Create a Spinbox to select password length (8 to 32 characters)
pass_len = IntVar()
length = Spinbox(
    root,
    from_=8,
    to_=32,
    textvariable=pass_len,
    width=15,
    font="arial 10",
    bg="#ffffff",
    fg="#333333",
)
length.pack(pady=5)

# Create a StringVar to store the generated password
pass_str = StringVar()

# Add a button to generate the password
Button(
    root,
    text="GENERATE PASSWORD",
    command=generate_password,
    font="arial 10 bold",
    bg="#4CAF50",
    fg="white",
    activebackground="#45a049",
).pack(pady=10)

# Add an entry field to display the generated password
Entry(
    root,
    textvariable=pass_str,
    font="arial 12",
    bg="#ffffff",
    fg="#333333",
    bd=2,
    relief="solid",
).pack(pady=10)

# Add a button to copy the password to the clipboard
Button(
    root,
    text="COPY TO CLIPBOARD",
    command=copy_password,
    font="arial 10 bold",
    bg="#008CBA",
    fg="white",
    activebackground="#007B9E",
).pack(pady=10)

# Add a footer label
Label(
    root,
    text="Made with ❤️ by Aya Nabil",
    font="arial 10",
    bg="#f0f0f0",
    fg="#777777",
).pack(side=BOTTOM, pady=10)

# Start the main event loop
root.mainloop()
