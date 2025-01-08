# Importing necessary libraries
import tkinter as tk  # Importing tkinter with an alias for better readability
from tkinter import messagebox  # For displaying alerts
import datetime  # For handling date and time
import time  # For time-related functions
import winsound  # For playing sound (Windows only)


# Function to trigger the alarm
def alarm(set_alarm_timer):
    """
    This function checks the current time and compares it with the set alarm time.
    When the time matches, it plays a sound and displays a message.
    """
    while True:
        time.sleep(1)  # Wait for 1 second before checking again
        current_time = datetime.datetime.now().strftime(
            "%H:%M:%S"
        )  # Get current time in HH:MM:SS format
        print(f"Current Time: {current_time}")  # Print current time for debugging
        if (
            current_time == set_alarm_timer
        ):  # Check if current time matches the alarm time
            print("Time to Wake up!")  # Print a message to the console
            winsound.PlaySound("sound.wav", winsound.SND_ASYNC)  # Play the alarm sound
            messagebox.showinfo("Alarm", "Time to Wake up!")  # Show a pop-up message
            break  # Exit the loop


# Function to get the alarm time from the user
def actual_time():
    """
    This function retrieves the alarm time entered by the user and calls the alarm function.
    """
    try:
        # Combine hours, minutes, and seconds into a single string
        set_alarm_timer = f"{hour.get()}:{minute.get()}:{second.get()}"
        alarm(set_alarm_timer)  # Call the alarm function with the set time
    except Exception as e:
        messagebox.showerror(
            "Error", "Please enter valid time values!"
        )  # Show error if input is invalid


# Main application window
clock = tk.Tk()
clock.title("Egyptian Alarm Clock")  # Set the title of the window
clock.geometry("400x250")  # Set the size of the window
clock.configure(bg="#f0e68c")  # Set background color to a sandy yellow (Egyptian theme)

# Labels and instructions for the user
tk.Label(
    clock,
    text="Welcome to the Egyptian Alarm Clock!",
    font=("Helvetica", 14, "bold"),
    bg="#f0e68c",
    fg="#8b4513",
).pack(pady=10)
tk.Label(
    clock,
    text="Enter time in 24-hour format:",
    font=("Arial", 10),
    bg="#f0e68c",
    fg="#8b4513",
).pack()

# Labels for hour, minute, and second inputs
tk.Label(
    clock, text="Hour   Minute   Second", font=("Arial", 10), bg="#f0e68c", fg="#8b4513"
).pack(pady=5)

# Variables to store user input for hour, minute, and second
hour = tk.StringVar()
minute = tk.StringVar()
second = tk.StringVar()

# Entry fields for hour, minute, and second
tk.Entry(clock, textvariable=hour, bg="#fffacd", width=5, font=("Arial", 12)).place(
    x=120, y=100
)  # Hour input
tk.Entry(clock, textvariable=minute, bg="#fffacd", width=5, font=("Arial", 12)).place(
    x=180, y=100
)  # Minute input
tk.Entry(clock, textvariable=second, bg="#fffacd", width=5, font=("Arial", 12)).place(
    x=240, y=100
)  # Second input

# Button to set the alarm
tk.Button(
    clock,
    text="Set Alarm",
    command=actual_time,
    bg="#8b4513",
    fg="white",
    font=("Arial", 12),
).place(x=150, y=150)

# Footer with copyright information
tk.Label(
    clock,
    text="© 2025 Aya Nabil. All rights reserved.",
    font=("Arial", 8),
    bg="#f0e68c",
    fg="#8b4513",
).pack(side="bottom", pady=10)

# Run the application
clock.mainloop()
