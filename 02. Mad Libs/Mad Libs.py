# 1. Import Required Modules
from tkinter import Tk, Label, Button, Text, Toplevel, Entry, END

# 2. Create the Main Window
root = Tk()
root.geometry("400x500")
root.title("Aya Nabil - Mad Libs Generator")

## Add Title and Instructions
Label(
    root, text="Mad Libs Generator\nHave Fun!", font="Arial 20 bold").pack(pady=10)
Label(root, text="Click Any One:", font="Arial 15 bold").pack(pady=5)

# Create a Text Box to Display the Output
output_box = Text(root, height=15, width=50, wrap="word", font="Arial 12")
output_box.pack(pady=10)

def display_story(story):
    """Helper function to display the story in the text box."""
    output_box.delete("1.0", END)
    output_box.insert(END, story)

# Input Window Generator
def input_window(title, prompts, callback):
    """Create a popup window for inputs."""
    window = Toplevel(root)
    window.title(title)
    inputs = []

    for i, prompt in enumerate(prompts):
        Label(window, text=prompt, font="Arial 12").grid(row=i, column=0, pady=5, padx=5)
        entry = Entry(window, font="Arial 12", width=30)
        entry.grid(row=i, column=1, pady=5, padx=5)
        inputs.append(entry)

    def submit():
        data = [entry.get() for entry in inputs]
        window.destroy()
        callback(data)

    Button(window, text="Submit", font="Arial 12", command=submit).grid(row=len(prompts), column=0, columnspan=2, pady=10)

# Define Mad Lib Functions
def madlib1():
    input_window("Mad Lib 1", [
        "Enter an animal name:", "Enter a profession name:",
        "Enter a piece of cloth:", "Enter a thing:",
        "Enter a name:", "Enter a place name:",
        "Enter a verb ending in 'ing':", "Enter a food name:"
    ], lambda data: display_story(
        f"Say {data[7]}, the photographer said as the camera flashed! {data[4]} and I had "
        f"gone to {data[5]} to get our photos taken on my birthday. The first photo we "
        f"really wanted was a picture of us dressed as {data[0]} pretending to be a {data[1]}. "
        f"When we saw the second photo, it was exactly what I wanted. We both looked like "
        f"{data[3]} wearing {data[2]} and {data[6]} — exactly what I had in mind!"
    ))

def madlib2():
    input_window("Mad Lib 2", [
        "Enter an adjective:", "Enter a color:", "Enter a thing:",
        "Enter a place:", "Enter a person's name:", "Enter another adjective:",
        "Enter an insect:", "Enter a food name:", "Enter a verb:"
    ], lambda data: display_story(
        f"Last night I dreamed I was a {data[0]} butterfly with {data[1]} splotches that looked like {data[2]}. "
        f"I flew to {data[3]} with my best friend {data[4]}, who was a {data[5]} {data[6]}. "
        f"We ate some {data[7]} when we got there and then decided to {data[8]}. The dream ended "
        f"when I said, 'Let's {data[8]} again!'"
    ))

def madlib3():
    input_window("Mad Lib 3", [
        "Enter a person's name:", "Enter a color:", "Enter a food name:",
        "Enter an adjective:", "Enter a thing:", "Enter a place:",
        "Enter a verb:", "Enter an adverb:", "Enter another food name:", "Enter another thing:"
    ], lambda data: display_story(
        f"Today we picked apples from {data[0]}'s orchard. I had no idea there were so many varieties of apples. "
        f"I ate {data[1]} apples straight off the tree that tasted like {data[2]}. Then there was a {data[3]} apple "
        f"that looked like a {data[4]}.\n\nWhen our bags were full, we went on a free hayride to {data[5]} and back. "
        f"It ended at a hay pile where we got to {data[6]} {data[7]}.\n\nI can hardly wait to get home and cook with "
        f"the apples. We are going to make apple {data[8]} and {data[9]} pies!"
    ))

# 5. Create Buttons for Each Mad Lib
Button(
    root, text="The Photographer", font="Arial 15", command=madlib1, bg="ghost white"
).pack(pady=5)
Button(
    root, text="Apple and Apple", font="Arial 15", command=madlib3, bg="ghost white"
).pack(pady=5)
Button(
    root, text="The Butterfly", font="Arial 15", command=madlib2, bg="ghost white"
).pack(pady=5)

# 6. Run the Application
root.mainloop()