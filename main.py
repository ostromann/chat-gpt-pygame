import pygame
from player import Player
from input import Input

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

# Set the platform properties
platform_width = 200
platform_height = 20
platform_color = (0, 255, 0)
platform_pos = [200, 300]

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
    if (player.y + player.height > platform_pos[1] and
        player.x + player.width > platform_pos[0] and
            player.x < platform_pos[0] + platform_width):
        player.velocity[1] = 0
        player.y = platform_pos[1] - player.height

    # Draw the background
    screen.fill(bg_color)

    # Draw the platform
    pygame.draw.rect(screen, platform_color, pygame.Rect(
        platform_pos[0], platform_pos[1], platform_width, platform_height))

    # Draw the player
    player.draw(screen)

    # Update the display
    pygame.display.flip()

    # Limit the FPS
    clock.tick(60)

# Quit Pygame
pygame.quit()
