# Import necessary modules
import tkinter as tk
from tkinter import messagebox, filedialog
from pytube import YouTube


# Function to download the YouTube video
def download_video():
    try:
        # Get the URL from the entry widget
        url = YouTube(str(link.get()))
        # Ask the user to choose the download location
        download_path = filedialog.askdirectory(title="Select Download Location")
        if download_path:
            # Get the first available video stream and download it to the selected location
            video = url.streams.first()
            video.download(download_path)
            # Show a success message
            messagebox.showinfo("Success", "Video Downloaded Successfully!")
        else:
            # Show a message if no location is selected
            messagebox.showwarning("Warning", "No download location selected!")
    except Exception as e:
        # Show an error message if something goes wrong
        messagebox.showerror("Error", f"An error occurred: {e}")


# Create the main application window
root = tk.Tk()
root.geometry("500x300")  # Set the window size
root.resizable(0, 0)  # Make the window non-resizable
root.title("Egyptian YouTube Video Downloader")  # Set the window title

# Set an Egyptian-themed background color
root.configure(bg="#8B4513")  # Saddle Brown for a rich, earthy Egyptian feel

# Add a title label with Egyptian-themed styling
title_label = tk.Label(
    root,
    text="YouTube Video Downloader",
    font=("Arial", 20, "bold"),
    bg="#8B4513",
    fg="#FFD700",  # Gold color for an Egyptian feel
)
title_label.pack(pady=20)

# Create a frame to center the widgets
center_frame = tk.Frame(root, bg="#8B4513")
center_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Add a label and entry widget for the YouTube link
link_label = tk.Label(
    center_frame,
    text="Paste Link Here:",
    font=("Arial", 15, "bold"),
    bg="#8B4513",
    fg="#FFFFFF",  # White color for contrast
)
link_label.pack(pady=10)

# Create a StringVar to store the link
link = tk.StringVar()

# Add an entry widget for the user to paste the YouTube link
link_entry = tk.Entry(
    center_frame,
    width=50,
    textvariable=link,
    font=("Arial", 12),
    bg="#FFFFFF",  # White background for the entry
    fg="#000000",  # Black text color
)
link_entry.pack(pady=10)

# Add a download button with Egyptian-themed styling
download_button = tk.Button(
    center_frame,
    text="DOWNLOAD",
    font=("Arial", 15, "bold"),
    bg="#FF4500",  # Orange-Red color for a vibrant button
    fg="#FFFFFF",  # White text color
    padx=20,
    command=download_video,
)
download_button.pack(pady=20)

# Add a copyright label at the bottom
copyright_label = tk.Label(
    root,
    text="© 2025 Aya Nabil. All rights reserved.",
    font=("Arial", 10),
    bg="#8B4513",
    fg="#FFFFFF",
)
copyright_label.pack(side=tk.BOTTOM, pady=10)

# Start the main event loop
root.mainloop()
