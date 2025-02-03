from tkinter import *
from math import factorial

# Initialize the main window
root = Tk()
root.title("Python Calculator - By Aya Nabil")
root.geometry("400x500")  # Set a fixed window size
root.resizable(False, False)  # Disable resizing
root.configure(bg="#2E3440")  # Set a dark theme background

# Custom colors for the calculator
BG_COLOR = "#2E3440"
BUTTON_COLOR = "#4C566A"
TEXT_COLOR = "#D8DEE9"
DISPLAY_COLOR = "#3B4252"
ERROR_COLOR = "#BF616A"

# Adding the input field (display)
display = Entry(
    root,
    font=("Arial", 24),
    bg=DISPLAY_COLOR,
    fg=TEXT_COLOR,
    bd=10,
    relief=FLAT,
    justify=RIGHT,
)
display.grid(row=0, column=0, columnspan=6, sticky=N + E + W + S, padx=10, pady=10)


# Function to insert numbers into the display
def get_variables(num):
    global i
    display.insert(i, num)
    i += 1


# Function to insert operations into the display
def get_operation(operator):
    global i
    length = len(operator)
    display.insert(i, operator)
    i += length


# Function to clear the display
def clear_all():
    display.delete(0, END)


# Function to undo the last input
def undo():
    entire_string = display.get()
    if len(entire_string):
        new_string = entire_string[:-1]
        clear_all()
        display.insert(0, new_string)
    else:
        clear_all()
        display.insert(0, "Error")


# Function to calculate the result
def calculate():
    entire_string = display.get()
    try:
        # Use eval() to evaluate the expression
        result = eval(entire_string)
        clear_all()
        display.insert(0, result)
    except Exception:
        clear_all()
        display.insert(0, "Error")


# Function to calculate factorial
def fact():
    entire_string = display.get()
    try:
        result = factorial(int(entire_string))
        clear_all()
        display.insert(0, result)
    except Exception:
        clear_all()
        display.insert(0, "Error")


# Button layout
buttons = [
    ("1", 2, 0),
    ("2", 2, 1),
    ("3", 2, 2),
    ("4", 3, 0),
    ("5", 3, 1),
    ("6", 3, 2),
    ("7", 4, 0),
    ("8", 4, 1),
    ("9", 4, 2),
    ("0", 5, 1),
    (".", 5, 2),
    ("+", 2, 3),
    ("-", 3, 3),
    ("*", 4, 3),
    ("/", 5, 3),
    ("AC", 5, 0),
    ("<-", 2, 5),
    ("x!", 3, 5),
    ("(", 4, 4),
    (")", 4, 5),
    ("%", 3, 4),
    ("π", 2, 4),
    ("^2", 5, 5),
    ("exp", 5, 4),
    ("=", 6, 0, 1, 6),  # Spanning 6 columns for the '=' button
]

# Create buttons dynamically
for button in buttons:
    text, row, col, *args = button
    if text == "=":
        Button(
            root,
            text=text,
            font=("Arial", 18),
            bg=ERROR_COLOR,
            fg=TEXT_COLOR,
            bd=5,
            relief=RAISED,
            command=calculate,
        ).grid(
            row=row,
            column=col,
            columnspan=args[0],
            sticky=N + E + W + S,
            padx=5,
            pady=5,
        )
    else:
        Button(
            root,
            text=text,
            font=("Arial", 18),
            bg=BUTTON_COLOR,
            fg=TEXT_COLOR,
            bd=5,
            relief=RAISED,
            command=lambda t=text: get_variables(t)
            if t.isdigit() or t == "."
            else get_operation(t)
            if t in ["+", "-", "*", "/", "(", ")", "%", "^2", "exp", "π"]
            else clear_all()
            if t == "AC"
            else undo()
            if t == "<-"
            else fact()
            if t == "x!"
            else None,
        ).grid(row=row, column=col, sticky=N + E + W + S, padx=5, pady=5)

# Initialize the index for input
i = 0

# Start the main loop
root.mainloop()
