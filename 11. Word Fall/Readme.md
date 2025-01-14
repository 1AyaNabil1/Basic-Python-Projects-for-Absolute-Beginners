# Word Fall Game 🎮💡

**By Aya Nabil**

## 😎 About the Project

The **Word Fall Game** is a fun, interactive Python game where players race against time to type falling words correctly before they reach the bottom of the screen. It's a great way to practice typing skills while having fun. Built using Pygame, this project is perfect for Python enthusiasts looking to explore game development.

---

## 🌟 Key Features

- **Dynamic Gameplay**: Randomly generated words fall at increasing speeds, challenging players to improve their typing speed and accuracy.
- **Interactive GUI**: Developed using Pygame for a visually appealing and responsive experience.
- **Start and Game Over Screens**: Smooth transitions and clear instructions for players.
- **Score Tracking**: Earn points for every word typed correctly.
- **Error Handling**: Resets input for incorrect guesses.

---

## 🔧 Technologies Used

- **Python**: The core language used for development.
- **Pygame**: A powerful library for game creation and graphical interfaces.

---

## 🚪 Prerequisites

Ensure you have the following installed:

- **Python 3.x**: [Download Python](https://www.python.org/downloads/)
- **Pygame Library**: Install it using the command:

    ```bash
    pip install pygame
    ```

---

## 🔄 How to Run the Game

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/your-repo-link/word-fall-game
    cd word-fall-game
    ```

2. **Run the Game**:
    Execute the following command in your terminal:
    ```bash
    python word_fall_game.py
    ```

3. **Play the Game**:
    - Press any key to start the game.
    - Type the falling words correctly before they reach the bottom.
    - Your score increases with each correct word typed.
    - The game ends if a word reaches the bottom of the screen.

---

## 🕵️ How It Works

1. **Word Generation**:
    - Randomly selects a word from a predefined list.
    - Displays the word at a random horizontal position at the top of the screen.

2. **Falling Mechanics**:
    - Words fall vertically at a constant speed that increases as the game progresses.

3. **Player Interaction**:
    - Players type the falling words using their keyboard.
    - Correct input earns points and generates a new word.
    - Incorrect input resets the player's input field.

4. **Game States**:
    - Start Screen: Displays instructions and waits for the player to start.
    - Main Game: Active gameplay.
    - Game Over Screen: Displays the final score and allows players to restart.

---
## 🖼 Project Output

### Main Window

<p align="center">
  <img src="img/image.png" alt="Main Window">
</p>

### Game-Over Window
<p align="center">
  <img src="img/img2.png" alt="Main Window">
</p>

---

## 🌋 Code Highlights

- **Word Generation**:
    ```python
    def new_word():
        global displayword, x_cor, y_cor
        x_cor = random.randint(100, WIDTH - 100)  # Random x-coordinate
        y_cor = 0  # Start at the top
        displayword = random.choice(words)  # Randomly select a word
    ```

- **Falling Mechanics**:
    ```python
    y_cor += word_speed
    if y_cor > HEIGHT:
        game_over = True
    ```

- **Player Input**:
    ```python
    if displayword.startswith(yourword):
        if displayword == yourword:
            score += len(displayword)  # Increase score
            yourword = ""  # Reset input
            new_word()  # Get a new word
    else:
        yourword = ""  # Reset input if incorrect
    ```

---

## 📅 Future Enhancements

- Add more words and difficulty levels.
- Introduce power-ups and penalties.
- Enhance the graphics with animations and themes.
- Implement a leaderboard for high scores.

---

## 🚀 Ready to Play?

Get started now and enjoy improving your typing skills in a fun and engaging way! If you liked this project, feel free to star the repository and contribute. Happy gaming! 😄

---

## 🔗 Resources

- [Python Documentation](https://docs.python.org/3/)
- [Pygame Documentation](https://www.pygame.org/docs/)

---

## ✨ Credits

This project is proudly developed by `Aya Nabil`.

**Stay tuned for more exciting projects and updates! 😊**
