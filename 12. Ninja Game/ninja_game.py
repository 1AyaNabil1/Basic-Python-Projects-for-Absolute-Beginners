import pygame
import sys
import random
import os

# Game constants
WIDTH = 800
HEIGHT = 500
FPS = 60
PLAYER_LIVES = 3
SCORE = 0
FRUITS = ["melon", "orange", "pomegranate", "guava", "bomb"]

# Initialize Pygame
pygame.init()

# Set up the display
game_display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("FRUIT NINJA - By Aya Nabil")
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
PURPLE = (128, 0, 128)
PINK = (255, 192, 203)


# Load images
def load_image(path):
    if os.path.exists(path):
        return pygame.image.load(path)
    return None


fruit_images = {
    "melon": load_image("images/melon.png"),
    "orange": load_image("images/orange.png"),
    "pomegranate": load_image("images/pomegranate.png"),
    "guava": load_image("images/guava.png"),
    "bomb": load_image("images/bomb.png"),
}

# Fallback colors if images are missing
fruit_colors = {
    "melon": GREEN,
    "orange": ORANGE,
    "pomegranate": RED,
    "guava": YELLOW,
    "bomb": BLACK,
}

# Load sounds
pygame.mixer.init()
cut_sound = (
    pygame.mixer.Sound("sounds/cut.wav") if os.path.exists("sounds/cut.wav") else None
)
bomb_sound = (
    pygame.mixer.Sound("sounds/bomb.wav") if os.path.exists("sounds/bomb.wav") else None
)
background_music = (
    pygame.mixer.Sound("sounds/background.mp3")
    if os.path.exists("sounds/background.mp3")
    else None
)

# Data structure to store fruit information
data = {}

# Game state
game_over = False
game_running = False
paused = False
start_time = 0


def generate_random_fruit(fruit):
    """
    Generates random positions, speeds, and colors for a fruit or bomb.
    """
    data[fruit] = {
        "image": fruit_images[fruit],
        "color": fruit_colors[fruit],
        "radius": random.randint(20, 40),  # Random size for the fruit
        "x": random.randint(100, WIDTH - 100),
        "y": HEIGHT,  # Start from the bottom of the screen
        "speed_x": random.randint(-5, 5),
        "speed_y": random.randint(-40, -30),  # Easy mode speed
        "throw": False,  # Whether the fruit is in motion
        "t": 0,  # Time counter for physics
        "hit": False,  # Whether the fruit has been hit
    }

    # Randomly decide if the fruit should be thrown
    if random.random() >= 0.5:  # 50% chance to throw
        data[fruit]["throw"] = True


def draw_text(display, text, size, x, y, color=WHITE):
    """
    Draws text on the screen.
    """
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    display.blit(text_surface, text_rect)


def draw_lives(display, x, y, lives):
    """
    Draws the player's lives on the screen using small hearts.
    """
    for i in range(lives):
        pygame.draw.circle(display, RED, (x + 35 * i, y), 10)


def show_start_menu():
    """
    Displays the start menu.
    """
    game_display.fill(BLACK)
    draw_text(game_display, "FRUIT NINJA", 64, WIDTH // 2, HEIGHT // 4, YELLOW)
    draw_text(game_display, "Press SPACE to Start", 40, WIDTH // 2, HEIGHT // 2, WHITE)
    draw_text(game_display, "Press H for Help", 24, WIDTH // 2, HEIGHT - 50, WHITE)
    pygame.display.flip()


def show_help_screen():
    """
    Displays the help screen with instructions.
    """
    game_display.fill(BLACK)
    draw_text(game_display, "HOW TO PLAY", 64, WIDTH // 2, HEIGHT // 4, YELLOW)
    draw_text(
        game_display, "Click on fruits to cut them.", 32, WIDTH // 2, HEIGHT // 2, WHITE
    )
    draw_text(
        game_display,
        "Avoid bombs or lose a life.",
        32,
        WIDTH // 2,
        HEIGHT // 2 + 40,
        WHITE,
    )
    draw_text(
        game_display,
        "Press P to pause/resume.",
        32,
        WIDTH // 2,
        HEIGHT // 2 + 80,
        WHITE,
    )
    draw_text(
        game_display, "Press any key to go back.", 24, WIDTH // 2, HEIGHT - 50, WHITE
    )
    pygame.display.flip()


def show_gameover_screen(score, survival_time):
    """
    Displays the game over screen with the final score and survival time.
    """
    game_display.fill(BLACK)
    draw_text(game_display, "GAME OVER!", 64, WIDTH // 2, HEIGHT // 4, RED)
    draw_text(
        game_display, f"Final Score: {score}", 40, WIDTH // 2, HEIGHT // 2, YELLOW
    )
    draw_text(
        game_display,
        f"Survival Time: {survival_time:.1f} seconds",
        40,
        WIDTH // 2,
        HEIGHT // 2 + 50,
        WHITE,
    )
    draw_text(
        game_display,
        "Press R to restart or Q to quit",
        24,
        WIDTH // 2,
        HEIGHT * 3 // 4,
        WHITE,
    )
    pygame.display.flip()


# Start menu loop
show_start_menu()
waiting = True
while waiting:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  # Start game
                waiting = False
            elif event.key == pygame.K_h:  # Show help screen
                show_help_screen()
                waiting_for_key = True
                while waiting_for_key:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                        if event.type == pygame.KEYDOWN:
                            waiting_for_key = False
                show_start_menu()

# Initialize fruits
for fruit in FRUITS:
    generate_random_fruit(fruit)

# Play background music
if background_music:
    background_music.play(-1)  # Loop indefinitely

# Main game loop
start_time = pygame.time.get_ticks()  # Track game start time
while True:
    if game_over:
        survival_time = (
            pygame.time.get_ticks() - start_time
        ) / 1000  # Calculate survival time
        show_gameover_screen(SCORE, survival_time)
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:  # Restart game
                        game_over = False
                        PLAYER_LIVES = 3
                        SCORE = 0
                        start_time = pygame.time.get_ticks()
                        for fruit in FRUITS:
                            generate_random_fruit(fruit)
                        waiting = False
                    elif event.key == pygame.K_q:  # Quit game
                        pygame.quit()
                        sys.exit()

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:  # Pause/resume game
                paused = not paused

    if paused:
        draw_text(game_display, "PAUSED", 64, WIDTH // 2, HEIGHT // 2, WHITE)
        pygame.display.flip()
        continue

    # Update game display
    game_display.fill(BLACK)  # Clear the screen
    draw_text(game_display, f"Score: {SCORE}", 32, 100, 10, GREEN)
    draw_text(game_display, f"Lives: {PLAYER_LIVES}", 32, WIDTH - 150, 10, RED)
    draw_text(
        game_display,
        f"Time: {(pygame.time.get_ticks() - start_time) / 1000:.1f}s",
        32,
        WIDTH // 2,
        10,
        WHITE,
    )

    # Update fruit positions
    for key, value in data.items():
        if value["throw"]:
            value["x"] += value["speed_x"]
            value["y"] += value["speed_y"]
            value["speed_y"] += 0.5 * value["t"]  # Simulate gravity
            value["t"] += 1

            if value["y"] <= HEIGHT:
                if value["image"]:
                    game_display.blit(
                        value["image"], (int(value["x"]), int(value["y"]))
                    )
                else:
                    pygame.draw.circle(
                        game_display,
                        value["color"],
                        (int(value["x"]), int(value["y"])),
                        value["radius"],
                    )
            else:
                generate_random_fruit(key)

            # Check for mouse clicks (fruit cuts)
            mouse_pos = pygame.mouse.get_pos()
            if (
                not value["hit"]
                and (value["x"] < mouse_pos[0] < value["x"] + 50)
                and (value["y"] < mouse_pos[1] < value["y"] + 50)
            ):
                if key == "bomb":
                    PLAYER_LIVES -= 1
                    if bomb_sound:
                        bomb_sound.play()
                    if PLAYER_LIVES == 0:
                        game_over = True
                else:
                    SCORE += 1
                    if cut_sound:
                        cut_sound.play()

                value["hit"] = True
                value["throw"] = False  # Stop the fruit from moving
        else:
            generate_random_fruit(key)

    pygame.display.update()
    clock.tick(FPS)
