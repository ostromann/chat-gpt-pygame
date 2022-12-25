from my_platform import Platform
from input import Input
from player import Player
import pygame

# Initialize Pygame
pygame.init()

# Set the window size
window_size = (640, 480)

# Create the window
screen = pygame.display.set_mode(window_size)

# Set the window title
pygame.display.set_caption("My Game")

# Set the background color
bg_color = (255, 255, 255)

# Create the platforms
platforms = [
    Platform(200, 300, 200, 20, (0, 255, 0)),
    Platform(400, 200, 200, 20, (0, 255, 0)),
    Platform(100, 100, 200, 20, (0, 255, 0)),
]

# Create the player
player = Player(100, 100, 50, 50, (0, 0, 255))

# Create the input handler
input = Input()

# Set the FPS clock
clock = pygame.time.Clock()

# Run the game loop
running = True
while running:
    # Handle events
    running = input.handle_events()

    # Update the player velocity based on the input
    player.velocity[0] = 0
    if input.left:
        player.velocity[0] -= 5
    if input.right:
        player.velocity[0] += 5
    if input.up:
        player.velocity[1] = -10

    # Update the player
    player.update()

    # Check if the player is on a platform
    on_platform = False
    for platform in platforms:
        if (player.y + player.height > platform.y and
            player.x + player.width > platform.x and
                player.x < platform.x + platform.width):
            player.velocity[1] = 0
            player.y = platform.y - player.height
            on_platform = True
            break

    # Check if the player fell outside the screen
    if not on_platform and player.y > window_size[1]:
        # Restart the game
        player.x = 100
        player.y = 100
        player.velocity = [0, 0]

    # Draw the background
    screen.fill(bg_color)

    # Draw the platforms
    for platform in platforms:
        platform.draw(screen)

    # Draw the player
    player.draw(screen)

    # Update the display
    pygame.display.flip()

    # Limit the FPS
    clock.tick(60)

# Quit Pygame
pygame.quit()
