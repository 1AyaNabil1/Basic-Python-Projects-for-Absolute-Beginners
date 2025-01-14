import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH = 800
HEIGHT = 600
FPS = 60  # Frames per second
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
LIGHT_BLUE = (173, 216, 230)
DARK_BLUE = (0, 0, 139)

# Set up display
gameDisplay = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Word Fall Game - By Aya Nabil")
clock = pygame.time.Clock()

# Fonts
font_name = pygame.font.match_font("arial")
font = pygame.font.Font(font_name, 40)

# Game variables
word_speed = 2  # Speed at which words fall
score = 0
game_over = False
game_start = True
yourword = ""  # Player's current input

# List of words for the game
words = [
    "python",
    "programming",
    "game",
    "developer",
    "keyboard",
    "challenge",
    "creative",
    "beginner",
]


# Function to load a random word
def new_word():
    global displayword, x_cor, y_cor
    x_cor = random.randint(100, WIDTH - 100)  # Random x-coordinate
    y_cor = 0  # Start at the top
    displayword = random.choice(words)  # Randomly select a word


# Function to draw text on the screen
def draw_text(display, text, size, color, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    display.blit(text_surface, text_rect)


# Function to display the start screen
def start_screen():
    gameDisplay.fill(LIGHT_BLUE)
    draw_text(gameDisplay, "Word Fall Game", 64, DARK_BLUE, WIDTH / 2, HEIGHT / 4)
    draw_text(gameDisplay, "How to Play:", 40, BLACK, WIDTH / 2, HEIGHT / 2 - 50)
    draw_text(
        gameDisplay,
        "Type the falling words correctly",
        30,
        BLACK,
        WIDTH / 2,
        HEIGHT / 2,
    )
    draw_text(
        gameDisplay,
        "before they reach the bottom!",
        30,
        BLACK,
        WIDTH / 2,
        HEIGHT / 2 + 40,
    )
    draw_text(
        gameDisplay, "Press any key to start", 40, DARK_BLUE, WIDTH / 2, HEIGHT * 3 / 4
    )
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYUP:
                waiting = False


# Function to display the game over screen
def game_over_screen():
    gameDisplay.fill(LIGHT_BLUE)
    draw_text(gameDisplay, "GAME OVER!", 64, RED, WIDTH / 2, HEIGHT / 4)
    draw_text(gameDisplay, f"Score: {score}", 40, DARK_BLUE, WIDTH / 2, HEIGHT / 2)
    draw_text(
        gameDisplay,
        "Press any key to restart",
        40,
        DARK_BLUE,
        WIDTH / 2,
        HEIGHT * 3 / 4,
    )
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYUP:
                waiting = False


# Initialize the first word
new_word()

# Main game loop
while True:
    if game_start:
        start_screen()
        game_start = False
        game_over = False
        score = 0
        word_speed = 2
        yourword = ""
        new_word()

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:  # Allow backspace to delete letters
                yourword = yourword[:-1]
            else:
                yourword += event.unicode  # Add the pressed key to the player's input

            # Check if the player's input matches the word
            if displayword.startswith(yourword):
                if displayword == yourword:
                    score += len(displayword)  # Increase score
                    yourword = ""  # Reset input
                    new_word()  # Get a new word
            else:
                yourword = ""  # Reset input if incorrect

    # Update game display
    gameDisplay.fill(LIGHT_BLUE)  # Background color

    # Draw the falling word
    draw_text(gameDisplay, displayword, 40, DARK_BLUE, x_cor, y_cor)

    # Draw the player's input
    draw_text(gameDisplay, f"Your input: {yourword}", 30, BLACK, WIDTH / 2, HEIGHT - 50)

    # Draw the score
    draw_text(gameDisplay, f"Score: {score}", 30, GREEN, WIDTH / 2, 10)

    # Move the word down
    y_cor += word_speed

    # Check if the word has reached the bottom
    if y_cor > HEIGHT:
        game_over = True

    # Update the display
    pygame.display.flip()
    clock.tick(FPS)

    # Handle game over
    if game_over:
        game_over_screen()
        game_start = True
