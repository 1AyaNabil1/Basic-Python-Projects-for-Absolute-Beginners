import tkinter as tk
from tkinter import messagebox

# Initialize the main window
root = tk.Tk()
root.geometry("600x450")  # Adjusted window size for better spacing
root.config(bg="#2E3440")  # Modern dark theme
root.resizable(0, 0)  # Disable resizing
root.title("Aya Nabil - Address Book")

# Sample contact list with Egyptian-like names
contact_list = [
    ["Ahmed Hassan", "01012345678"],
    ["Mariam Ali", "01123456789"],
    ["Youssef Mahmoud", "01234567890"],
    ["Fatima Ibrahim", "01567891234"],
    ["Omar Khaled", "01098765432"],
    ["Layla Samir", "01187654321"],
]

# Variables to store user input
name_var = tk.StringVar()
number_var = tk.StringVar()

# Track the currently selected contact index
selected_index = None

# Constants for repeated values
FONT_LARGE = ("Arial", 12, "bold")
FONT_SMALL = ("Arial", 10)
BG_COLOR = "#2E3440"
FG_COLOR = "#D8DEE9"
ENTRY_BG = "#4C566A"
ENTRY_FG = "#ECEFF4"
BUTTON_BG = "#5E81AC"
BUTTON_FG = "#ECEFF4"
BUTTON_ACTIVE_BG = "#81A1C1"  # Active button color
BUTTON_RADIUS = 10  # Rounded corners radius


# Custom rounded button class
class RoundedButton(tk.Canvas):
    def __init__(self, master=None, text="", command=None, **kwargs):
        # Remove unsupported options from kwargs
        self.bg = kwargs.pop("bg", BUTTON_BG)  # Background color
        self.fg = kwargs.pop("fg", BUTTON_FG)  # Text color
        self.active_bg = kwargs.pop(
            "active_bg", BUTTON_ACTIVE_BG
        )  # Active background color
        self.radius = kwargs.pop("radius", BUTTON_RADIUS)  # Corner radius
        self.width = kwargs.pop("width", 100)  # Button width
        self.height = kwargs.pop("height", 30)  # Button height

        # Initialize the Canvas
        super().__init__(master, **kwargs)
        self.command = command
        self.text = text

        # Configure the canvas
        self.config(
            bg=BG_COLOR, highlightthickness=0, width=self.width, height=self.height
        )
        self.draw_button()
        self.bind("<Button-1>", self.on_click)

    def draw_button(self):
        """Draw the rounded button with text."""
        self.delete("all")
        self.create_rounded_rectangle(
            0, 0, self.width, self.height, radius=self.radius, fill=self.bg
        )
        self.create_text(
            self.width // 2,
            self.height // 2,
            text=self.text,
            font=FONT_SMALL,
            fill=self.fg,  # Use fg only here
        )

    def create_rounded_rectangle(self, x1, y1, x2, y2, radius=10, **kwargs):
        """Create a rounded rectangle."""
        points = [
            x1 + radius,
            y1,
            x2 - radius,
            y1,
            x2,
            y1,
            x2,
            y1 + radius,
            x2,
            y2 - radius,
            x2,
            y2,
            x2 - radius,
            y2,
            x1 + radius,
            y2,
            x1,
            y2,
            x1,
            y2 - radius,
            x1,
            y1 + radius,
            x1,
            y1,
        ]
        return self.create_polygon(points, **kwargs, smooth=True)

    def on_click(self, event):
        """Handle button click event."""
        if self.command:
            self.command()


# Frame for the contact list
frame = tk.Frame(root, bg=BG_COLOR)
frame.pack(side=tk.RIGHT, padx=20, pady=20)

# Scrollbar for the contact list
scroll = tk.Scrollbar(frame, orient=tk.VERTICAL)
select = tk.Listbox(
    frame,
    yscrollcommand=scroll.set,
    height=12,
    bg=ENTRY_BG,
    fg=ENTRY_FG,
    font=FONT_SMALL,
    selectbackground=BUTTON_BG,
)
scroll.config(command=select.yview)
scroll.pack(side=tk.RIGHT, fill=tk.Y)
select.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

# Bind listbox selection to display phone number
select.bind("<<ListboxSelect>>", lambda event: view_contact())


def selected():
    """Get the index of the currently selected contact."""
    global selected_index
    try:
        selected_index = int(select.curselection()[0])
        return selected_index
    except IndexError:
        selected_index = None
        return None


def add_contact():
    """Add a new contact to the list."""
    name = name_var.get()
    number = number_var.get()
    if name and number:  # Ensure both fields are filled
        contact_list.append([name, number])
        update_list()
        reset_fields()
    else:
        messagebox.showwarning("Input Error", "Please fill in both fields!")


def edit_contact():
    """Edit the currently selected contact."""
    global selected_index
    if selected_index is None:
        messagebox.showwarning("No Selection", "Please select a contact first!")
        return

    # Get the current contact details
    current_name, current_number = contact_list[selected_index]

    # Get the new values from the input fields
    new_name = name_var.get()
    new_number = number_var.get()

    # Check if any changes were made
    if new_name == current_name and new_number == current_number:
        messagebox.showinfo("No Changes", "No changes were made to the contact.")
        return

    # Update the contact
    if new_name:  # If the name is changed
        contact_list[selected_index][0] = new_name
    if new_number:  # If the number is changed
        contact_list[selected_index][1] = new_number

    update_list()
    messagebox.showinfo("Success", "Contact updated successfully!")


def delete_contact():
    """Delete the currently selected contact."""
    global selected_index
    if selected_index is None:
        messagebox.showwarning("No Selection", "Please select a contact first!")
        return

    del contact_list[selected_index]
    update_list()
    reset_fields()
    selected_index = None  # Reset the selected index


def view_contact():
    """View the selected contact's details."""
    global selected_index
    selected_index = selected()
    if selected_index is not None:
        name, number = contact_list[selected_index]
        name_var.set(name)
        number_var.set(number)


def reset_fields():
    """Clear the input fields."""
    name_var.set("")
    number_var.set("")


def update_list():
    """Update the contact list in the GUI."""
    contact_list.sort(key=lambda x: x[0])  # Sort by name
    select.delete(0, tk.END)
    for name, number in contact_list:
        select.insert(tk.END, name)


# Initialize the contact list
update_list()

# Labels and Entry fields
tk.Label(root, text="NAME", font=FONT_LARGE, bg=BG_COLOR, fg=FG_COLOR).place(x=30, y=20)
tk.Entry(root, textvariable=name_var, font=FONT_SMALL, bg=ENTRY_BG, fg=ENTRY_FG).place(
    x=150, y=20, width=200
)

tk.Label(root, text="PHONE NO.", font=FONT_LARGE, bg=BG_COLOR, fg=FG_COLOR).place(
    x=30, y=70
)
tk.Entry(
    root, textvariable=number_var, font=FONT_SMALL, bg=ENTRY_BG, fg=ENTRY_FG
).place(x=150, y=70, width=200)

# Buttons with rounded edges
RoundedButton(
    root,
    text="ADD",
    width=100,
    height=30,
    bg=BUTTON_BG,
    fg=BUTTON_FG,
    active_bg=BUTTON_ACTIVE_BG,
    command=add_contact,
).place(x=50, y=120)
RoundedButton(
    root,
    text="EDIT",
    width=100,
    height=30,
    bg=BUTTON_BG,
    fg=BUTTON_FG,
    active_bg=BUTTON_ACTIVE_BG,
    command=edit_contact,
).place(x=50, y=170)
RoundedButton(
    root,
    text="DELETE",
    width=100,
    height=30,
    bg=BUTTON_BG,
    fg=BUTTON_FG,
    active_bg=BUTTON_ACTIVE_BG,
    command=delete_contact,
).place(x=50, y=220)
RoundedButton(
    root,
    text="RESET",
    width=100,
    height=30,
    bg=BUTTON_BG,
    fg=BUTTON_FG,
    active_bg=BUTTON_ACTIVE_BG,
    command=reset_fields,
).place(x=50, y=270)
RoundedButton(
    root,
    text="EXIT",
    width=100,
    height=30,
    bg="#BF616A",
    fg=BUTTON_FG,
    active_bg="#D08770",
    command=root.destroy,
).place(x=50, y=320)

# Start the main event loop
root.mainloop()
