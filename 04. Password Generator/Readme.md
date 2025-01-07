# Password Generator in Python 🔐

**By Aya Nabil**

## 🧐 About the Project

The **Password Generator** is a simple yet powerful tool that helps you create strong and secure passwords. Built using Python and Tkinter, this project generates random passwords with a mix of uppercase letters, lowercase letters, digits, and special characters. It’s a perfect project for beginners to learn Python while building something practical and useful!

---

## 🌟 Why Use a Password Generator?

In today’s digital world, strong passwords are essential for protecting your online accounts. Instead of relying on weak or repetitive passwords, this tool helps you generate secure passwords instantly. By building this project, you’ll learn Python basics like **functions**, **random module**, and **GUI development** while creating a tool you can use every day.

----

## 🧩 Features

- **User-Friendly GUI**: Built with Tkinter for a clean and intuitive interface.
- **Customizable Password Length**: Choose a password length between 8 and 32 characters.
- **Strong Password Generation**: Passwords include uppercase letters, lowercase letters, digits, and special characters.
- **Copy to Clipboard**: Easily copy the generated password to your clipboard with one click.
- **Beginner-Friendly**: Perfect for learning Python basics like functions, event handling, and GUI development.

---

## 🛠️ Project Prerequisites

Before you start, ensure you have:

- **Basic Python Knowledge**: Familiarity with defining functions, handling user input, and working with strings.
- **Python Installed**: Ensure Python 3.x is installed on your system.
- **Tkinter**: Usually comes pre-installed with Python.
- **pyperclip**: Install it using ```pip install pyperclip```

---

### Python Concepts Used

- **Tkinter**: For creating the graphical user interface (GUI).
- **Random Module**: To generate random characters for the password.
- **String Module**: To access predefined character sets (uppercase, lowercase, digits, and punctuation).
- **Functions**: To organize code and handle password generation.
- **Event Handling**: Responding to button clicks and user input.

---

## 📂 Project File Structure

Here’s a step-by-step breakdown of how this project works:

1. **Import Required Modules:**

- ```tkinter``` For creating the GUI (windows, buttons, labels, etc.).
- ```random``` To generate random characters for the password.
- ```string``` To access predefined character sets.
- ```pyperclip``` To copy the password to the clipboard.

2. **Define Functions:**

- `generate_password()` Generates a random password with a mix of uppercase, lowercase, digits, and special characters.
- `copy_password()` Copies the generated password to the clipboard.

3. **Password Generation Logic:**

- The user selects the desired password length using a `Spinbox`.

- The program generates a password with at least one character from each category (uppercase, lowercase, digit, and special character).

- The password is displayed in an `Entry` widget.

4. **Interactive GUI:**

- Buttons for `GENERATE PASSWORD` and `COPY TO CLIPBOARD`.
- A `Spinbox` to select the password length.
- An `Entry` widget to display the generated password.

---

## 🚀 How to Run the Project

1. **Clone or Download the Repository**:

   ```bash
   git clone https://github.com/1AyaNabil1/Basic-Python-Projects-for-Absolute-Beginners.git
   
   cd Basic-Python-Projects-for-Absolute-Beginners/04.\ Password\ Generator

2. **Install Dependencies:**:

   ```python
   pip install pyperclip
    ```

3. **Run the Script:**

   ```bash
   python password_generator.py
4. **Follow the Prompts:**
    - Select the desired password length using the `Spinbox`.

   - Click **GENERATE PASSWORD** to create a new password.

    - Click **COPY TO CLIPBOARD** to copy the password to your clipboard.

---

## 📸 Project Output

### Example Gameplay

1. **Main Window**:
   ![Main Window](img/image.png)

2. **Generated Password**:
   ![Input Window](img/img%202.png)

3. **Copy to Clipboard:**
   ![Input Window](img/img%202.png)

---

## 📖 Summary

**With this project, you’ve learned how to:**

1. Create a simple GUI using Tkinter.

2. Use the ``random`` and `string` modules to generate random passwords.

3. Copy text to the clipboard using `pyperclip`.

4. Build a practical and interactive Python project from scratch.

---

## ✨ Credits

This project is proudly developed by `Aya Nabil`.

**Want to explore more beginner-friendly projects? Stay tuned! 😊**
