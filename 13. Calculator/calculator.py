from tkinter import *
import parser
from math import factorial

# Initialize the main window
root = Tk()
root.title("Python Calculator - By Aya Nabil")
root.geometry("400x500")  # Set a fixed window size
root.configure(bg="#2E3440")  # Dark background for a modern look

# Adding the input field
display = Entry(
    root, font=("Arial", 20), justify="right", bd=10, bg="#3B4252", fg="#ECEFF4"
)
display.grid(row=0, column=0, columnspan=6, sticky=N + E + W + S, padx=10, pady=10)

# Global variable to keep track of the current position in the input field
i = 0


# Function to add numbers and operators to the display
def get_variables(num):
    global i
    display.insert(i, num)
    i += 1


# Function to add operations to the display
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
        a = parser.expr(entire_string).compile()
        result = eval(a)
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


# Function to create a button with consistent styling
def create_button(text, command, row, column, columnspan=1, bg="#4C566A", fg="#ECEFF4"):
    button = Button(
        root,
        text=text,
        command=command,
        font=("Arial", 16),
        bg=bg,
        fg=fg,
        bd=5,
        relief="ridge",
    )
    button.grid(
        row=row,
        column=column,
        columnspan=columnspan,
        sticky=N + S + E + W,
        padx=5,
        pady=5,
    )
    return button


# Adding number buttons
create_button("1", lambda: get_variables(1), 1, 0)
create_button("2", lambda: get_variables(2), 1, 1)
create_button("3", lambda: get_variables(3), 1, 2)
create_button("4", lambda: get_variables(4), 2, 0)
create_button("5", lambda: get_variables(5), 2, 1)
create_button("6", lambda: get_variables(6), 2, 2)
create_button("7", lambda: get_variables(7), 3, 0)
create_button("8", lambda: get_variables(8), 3, 1)
create_button("9", lambda: get_variables(9), 3, 2)
create_button("0", lambda: get_variables(0), 4, 1)
create_button(".", lambda: get_variables("."), 4, 2)

# Adding operation buttons
create_button("+", lambda: get_operation("+"), 1, 3, bg="#5E81AC")
create_button("-", lambda: get_operation("-"), 2, 3, bg="#5E81AC")
create_button("*", lambda: get_operation("*"), 3, 3, bg="#5E81AC")
create_button("/", lambda: get_operation("/"), 4, 3, bg="#5E81AC")
create_button("(", lambda: get_operation("("), 1, 4, bg="#81A1C1")
create_button(")", lambda: get_operation(")"), 2, 4, bg="#81A1C1")
create_button("π", lambda: get_operation("*3.14"), 3, 4, bg="#81A1C1")
create_button("%", lambda: get_operation("%"), 4, 4, bg="#81A1C1")
create_button("^2", lambda: get_operation("**2"), 1, 5, bg="#81A1C1")
create_button("exp", lambda: get_operation("**"), 2, 5, bg="#81A1C1")
create_button("x!", lambda: fact(), 3, 5, bg="#81A1C1")
create_button("<-", lambda: undo(), 4, 5, bg="#BF616A")

# Adding the clear and equals buttons
create_button("AC", lambda: clear_all(), 5, 0, columnspan=2, bg="#BF616A")
create_button("=", lambda: calculate(), 5, 2, columnspan=4, bg="#88C0D0")

# Adding copyright label
copyright_label = Label(
    root, text="© 2023 Aya Nabil", font=("Arial", 10), bg="#2E3440", fg="#ECEFF4"
)
copyright_label.grid(row=6, column=0, columnspan=6, pady=10)

# Run the application
root.mainloop()
