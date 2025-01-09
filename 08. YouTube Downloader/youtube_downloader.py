# Import necessary modules
import tkinter as tk
from tkinter import messagebox
from pytube import YouTube


# Function to download the YouTube video
def download_video():
    try:
        # Get the URL from the entry widget
        url = YouTube(str(link.get()))
        # Get the first available video stream and download it
        video = url.streams.first()
        video.download()
        # Show a success message
        messagebox.showinfo("Success", "Video Downloaded Successfully!")
    except Exception as e:
        # Show an error message if something goes wrong
        messagebox.showerror("Error", f"An error occurred: {e}")


# Create the main application window
root = tk.Tk()
root.geometry("500x300")  # Set the window size
root.resizable(0, 0)  # Make the window non-resizable
root.title("Egyptian YouTube Video Downloader")  # Set the window title

# Set an Egyptian-themed background color
root.configure(bg="#1E90FF")  # Dodger Blue for a vibrant look

# Add a title label with Egyptian-themed styling
title_label = tk.Label(
    root,
    text="YouTube Video Downloader",
    font=("Arial", 20, "bold"),
    bg="#1E90FF",
    fg="#FFD700",  # Gold color for an Egyptian feel
)
title_label.pack(pady=10)

# Add a label and entry widget for the YouTube link
link_label = tk.Label(
    root,
    text="Paste Link Here:",
    font=("Arial", 15, "bold"),
    bg="#1E90FF",
    fg="#FFFFFF",  # White color for contrast
)
link_label.place(x=160, y=60)

# Create a StringVar to store the link
link = tk.StringVar()

# Add an entry widget for the user to paste the YouTube link
link_entry = tk.Entry(
    root,
    width=70,
    textvariable=link,
    font=("Arial", 12),
    bg="#FFFFFF",  # White background for the entry
    fg="#000000",  # Black text color
)
link_entry.place(x=32, y=90)

# Add a download button with Egyptian-themed styling
download_button = tk.Button(
    root,
    text="DOWNLOAD",
    font=("Arial", 15, "bold"),
    bg="#FF4500",  # Orange-Red color for a vibrant button
    fg="#FFFFFF",  # White text color
    padx=10,
    command=download_video,
)
download_button.place(x=180, y=150)

# Add a copyright label at the bottom
copyright_label = tk.Label(
    root,
    text="© 2025 Aya Nabil. All rights reserved.",
    font=("Arial", 10),
    bg="#1E90FF",
    fg="#FFFFFF",
)
copyright_label.pack(side=tk.BOTTOM, pady=10)

# Start the main event loop
root.mainloop()
