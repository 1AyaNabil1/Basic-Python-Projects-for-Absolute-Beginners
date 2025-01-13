import base64
from tkinter import Tk, Label, Entry, Button, Frame, StringVar, CENTER, LEFT, BOTTOM

# Initialize the main window
root = Tk()
root.geometry("500x350")  # Slightly taller window for better spacing
root.resizable(0, 0)  # Disable resizing
root.title("Message Encoder and Decoder - Aya Nabil")
root.configure(bg="#2E3440")  # Dark background for a modern look

# Constants for repeated values
FONT_LARGE_BOLD = ("arial", 20, "bold")
FONT_MEDIUM_BOLD = ("arial", 12, "bold")
FONT_SMALL = ("arial", 10)
FONT_SMALL_BOLD = ("arial", 10, "bold")
BG_COLOR = "#2E3440"
FG_COLOR = "#D8DEE9"
ENTRY_BG = "#4C566A"
ENTRY_FG = "#ECEFF4"

# Title and subtitle labels
Label(
    root,
    text="Message Encoder and Decoder",
    font=FONT_LARGE_BOLD,
    bg=BG_COLOR,
    fg="#88C0D0",
).pack(pady=10)
Label(root, text="© Aya Nabil", font=FONT_SMALL, bg=BG_COLOR, fg=FG_COLOR).pack(
    side=BOTTOM, pady=10
)

# Variables to store user input and results
Text = StringVar()
private_key = StringVar()
mode = StringVar()
Result = StringVar()


# Function to encode a message
def encode(key, message):
    """
    Encodes the message using a simple substitution cipher and base64 encoding.
    :param key: The private key for encoding.
    :param message: The message to encode.
    :return: The encoded message.
    """
    enc = []
    for i in range(len(message)):
        key_c = key[
            i % len(key)
        ]  # Cycle through the key if it's shorter than the message
        enc.append(chr((ord(message[i]) + ord(key_c)) % 256))  # Perform substitution
    return base64.urlsafe_b64encode(
        "".join(enc).encode()
    ).decode()  # Base64 encode the result


# Function to decode a message
def decode(key, message):
    """
    Decodes the message using the private key and base64 decoding.
    :param key: The private key for decoding.
    :param message: The message to decode.
    :return: The decoded message.
    """
    try:
        # Add padding to the message if necessary
        padding = len(message) % 4
        if padding:
            message += "=" * (4 - padding)
        decoded_message = base64.urlsafe_b64decode(
            message
        ).decode()  # Base64 decode the message
        dec = []
        for i in range(len(decoded_message)):
            key_c = key[i % len(key)]  # Cycle through the key
            dec.append(
                chr((256 + ord(decoded_message[i]) - ord(key_c)) % 256)
            )  # Reverse the substitution
        return "".join(dec)
    except Exception as e:
        return "Error: Invalid input for decoding"


# Function to handle mode selection (encode or decode)
def mode_handler():
    """
    Determines whether to encode or decode based on user input.
    Updates the Result variable with the output.
    """
    if mode.get() == "e":
        Result.set(encode(private_key.get(), Text.get()))  # Encode the message
    elif mode.get() == "d":
        Result.set(decode(private_key.get(), Text.get()))  # Decode the message
    else:
        Result.set("Invalid Mode")  # Handle invalid mode input


# Function to reset all fields
def reset():
    """
    Clears all input fields and the result.
    """
    Text.set("")
    private_key.set("")
    mode.set("")
    Result.set("")


# Function to exit the application
def exit_app():
    """
    Closes the application.
    """
    root.destroy()


# GUI Elements
Label(root, font=FONT_MEDIUM_BOLD, text="MESSAGE", bg=BG_COLOR, fg=FG_COLOR).place(
    x=60, y=60
)
Entry(root, font=FONT_SMALL, textvariable=Text, bg=ENTRY_BG, fg=ENTRY_FG).place(
    x=290, y=60
)

Label(root, font=FONT_MEDIUM_BOLD, text="KEY", bg=BG_COLOR, fg=FG_COLOR).place(
    x=60, y=90
)
Entry(root, font=FONT_SMALL, textvariable=private_key, bg=ENTRY_BG, fg=ENTRY_FG).place(
    x=290, y=90
)

Label(
    root,
    font=FONT_MEDIUM_BOLD,
    text="MODE (e-encode, d-decode)",
    bg=BG_COLOR,
    fg=FG_COLOR,
).place(x=60, y=120)
Entry(root, font=FONT_SMALL, textvariable=mode, bg=ENTRY_BG, fg=ENTRY_FG).place(
    x=290, y=120
)

Label(root, font=FONT_MEDIUM_BOLD, text="RESULT", bg=BG_COLOR, fg=FG_COLOR).place(
    x=60, y=150
)
Entry(root, font=FONT_SMALL_BOLD, textvariable=Result, bg=ENTRY_BG, fg=ENTRY_FG).place(
    x=290, y=150
)

# Centered Buttons
button_frame = Frame(root, bg=BG_COLOR)  # Frame to hold the buttons
button_frame.place(relx=0.5, rely=0.75, anchor=CENTER)  # Center the frame

Button(
    button_frame,
    font=FONT_SMALL_BOLD,
    text="RESULT",
    padx=10,
    bg="#5E81AC",
    fg=ENTRY_FG,
    command=mode_handler,
).pack(side=LEFT, padx=5)
Button(
    button_frame,
    font=FONT_SMALL_BOLD,
    text="RESET",
    width=6,
    bg="#A3BE8C",
    fg=BG_COLOR,
    command=reset,
).pack(side=LEFT, padx=5)
Button(
    button_frame,
    font=FONT_SMALL_BOLD,
    text="EXIT",
    width=6,
    bg="#BF616A",
    fg=ENTRY_FG,
    command=exit_app,
).pack(side=LEFT, padx=5)

# Start the main event loop
root.mainloop()
