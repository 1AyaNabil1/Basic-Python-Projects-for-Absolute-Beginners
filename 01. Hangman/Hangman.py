import random
import time


# Welcome message and introduction
def welcome_message():
    print("\nWelcome to the Hangman game by AyaNabil!\n")
    name = input("Enter your name: ")
    print(f"Hello, {name}! Best of Luck!")
    time.sleep(2)
    print("The game is about to start!\nLet's play Hangman!")
    time.sleep(2)


# Main function to initialize the game
def initialize_game():
    global word_to_guess, hidden_word, guessed_letters, attempts_left
    words = [
        "january",
        "border",
        "image",
        "film",
        "promise",
        "kids",
        "lungs",
        "doll",
        "rhyme",
        "damage",
        "plants",
    ]
    word_to_guess = random.choice(words)
    hidden_word = "_" * len(word_to_guess)
    guessed_letters = []
    attempts_left = 5


# Function to ask the user if they want to play again
def play_again_prompt():
    while True:
        play_again = input("\nDo you want to play again? (y/n): ").strip().lower()
        if play_again in ["y", "n"]:
            return play_again == "y"
        print("Invalid input. Please enter 'y' for yes or 'n' for no.")


# Display the current state of the hangman
def display_hangman(attempts):
    hangman_states = [
        """
           _____
          |
          |
          |
          |
          |
          |
        __|__
        """,
        """
           _____ 
          |     | 
          |     |
          |      
          |      
          |      
          |      
        __|__
        """,
        """
           _____ 
          |     | 
          |     |
          |     | 
          |      
          |      
          |      
        __|__
        """,
        """
           _____ 
          |     | 
          |     |
          |     | 
          |     O 
          |      
          |      
        __|__
        """,
        """
           _____ 
          |     | 
          |     |
          |     | 
          |     O 
          |    /|\\ 
          |    / \\ 
        __|__
        """,
    ]
    # Ensure the index does not exceed the length of the hangman states
    if attempts < len(hangman_states):
        print(hangman_states[attempts])


# The main game logic
def play_hangman():
    global word_to_guess, hidden_word, guessed_letters, attempts_left

    while attempts_left > 0:
        print(f"\nWord to guess: {hidden_word}")
        guess = input("Enter your guess (a single letter): ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print(f"You've already guessed '{guess}'. Try another letter.")
            continue

        guessed_letters.append(guess)

        if guess in word_to_guess:
            print(f"Good guess! '{guess}' is in the word.")
            hidden_word = "".join(
                [char if char in guessed_letters else "_" for char in word_to_guess]
            )
            if "_" not in hidden_word:
                print(f"\nCongrats! You've guessed the word: {word_to_guess}")
                break
        else:
            attempts_left -= 1
            print(f"Wrong guess! You have {attempts_left} attempts left.")
            display_hangman(5 - attempts_left)

    if attempts_left == 0:
        print(f"\nYou're out of attempts! The word was: {word_to_guess}")
        display_hangman(5)  # Display the final hangman state


# Main execution flow
def main():
    welcome_message()
    while True:
        initialize_game()
        play_hangman()
        if not play_again_prompt():
            print("\nThanks for playing! See you next time!")
            break


if __name__ == "__main__":
    main()
