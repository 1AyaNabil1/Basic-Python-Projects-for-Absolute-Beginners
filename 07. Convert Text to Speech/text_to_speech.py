import tkinter as tk
from tkinter import StringVar
from gtts import gTTS
import pygame
import os
import tempfile

# Initialize pygame mixer
pygame.mixer.init()

# Constants for repeated values
FONT_STYLE = "arial 15 bold"
AUDIO_FILE = os.path.join(tempfile.gettempdir(), "output.mp3")  # Save in temp directory

# Initialize the main window
root = tk.Tk()
root.geometry("400x350")  # Set window size
root.configure(bg="#2E86C1")  # Egyptian blue background
root.title("Text to Speech - Aya Nabil")  # Window title with your name

# Add a header label
header_label = tk.Label(
    root, text="TEXT TO SPEECH", font="arial 20 bold", bg="#2E86C1", fg="white"
)
header_label.pack(pady=10)

# Add a footer label with your copyright
footer_label = tk.Label(
    root, text="© 2025 Aya Nabil", font="arial 10 bold", bg="#2E86C1", fg="white"
)
footer_label.pack(side="bottom", pady=10)

# Variable to store user input
user_input = StringVar()

# Label to prompt the user to enter text
input_label = tk.Label(
    root, text="Enter Text Below:", font=FONT_STYLE, bg="#2E86C1", fg="white"
)
input_label.pack(pady=10)

# Entry field for user input
entry_field = tk.Entry(root, textvariable=user_input, width=40, font="arial 12")
entry_field.pack(pady=10)


# Function to convert text to speech
def text_to_speech():
    message = entry_field.get()  # Get text from the entry field
    if message:  # Check if the input is not empty
        if os.path.exists(AUDIO_FILE):  # Check if the file already exists
            os.remove(AUDIO_FILE)  # Delete the existing file
        speech = gTTS(text=message, lang="en")  # Convert text to speech
        speech.save(AUDIO_FILE)  # Save the audio file
        pygame.mixer.music.load(AUDIO_FILE)  # Load the audio file
        pygame.mixer.music.play()  # Play the audio file
        while pygame.mixer.music.get_busy():  # Wait for playback to finish
            pygame.time.Clock().tick(10)
        os.remove(AUDIO_FILE)  # Delete the file after playing
    else:
        user_input.set("Please enter some text!")  # Show error if input is empty


# Function to exit the application
def exit_app():
    root.destroy()  # Close the window


# Function to reset the input field
def reset_input():
    user_input.set("")  # Clear the entry field


# Frame to hold the buttons (for better alignment)
button_frame = tk.Frame(root, bg="#2E86C1")
button_frame.pack(pady=20)

# Button to play the text as speech
play_button = tk.Button(
    button_frame,
    text="PLAY",
    font=FONT_STYLE,
    command=text_to_speech,
    bg="#28B463",
    fg="white",
)
play_button.pack(side="left", padx=10)

# Button to exit the application
exit_button = tk.Button(
    button_frame,
    text="EXIT",
    font=FONT_STYLE,
    command=exit_app,
    bg="#CB4335",
    fg="white",
)
exit_button.pack(side="left", padx=10)

# Button to reset the input field
reset_button = tk.Button(
    button_frame,
    text="RESET",
    font=FONT_STYLE,
    command=reset_input,
    bg="#D4AC0D",
    fg="white",
)
reset_button.pack(side="left", padx=10)

# Start the main event loop
root.mainloop()
