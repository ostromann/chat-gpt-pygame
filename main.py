import pygame
from player import Player
from input import Input
from obstacles import Obstacle, Wall, Trap
import random

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

# Set the grid size
grid_size = (20, 20)

# Set the player starting position
player_pos = (10, 10)

# Create the player
player = Player(player_pos, grid_size, (0, 0, 255))

# Create the input handler
input = Input()

# Set the FPS clock
clock = pygame.time.Clock()

# Initialize the obstacles list
obstacles = []

# Run the game loop
running = True
while running:
    # Handle events
    running = input.handle_events()

    # Update the player velocity based on the input
    player.velocity[0] = 0
    player.velocity[1] = 0
    if input.left:
        player.velocity[0] -= 1
    if input.right:
        player.velocity[0] += 1
    if input.up:
        player.velocity[1] -= 1
    if input.down:
        player.velocity[1] += 1

    # Update the player position
    player.pos[0] += player.velocity[0]
    player.pos[1] += player.velocity[1]

    # Check if the player is out of bounds
    if player.pos[0] < 0:
        player.pos[0] = 0
    elif player.pos[0] > window_size[0] / grid_size[0] - 1:
        player.pos[0] = window_size[0] / grid_size[0] - 1
    if player.pos[1] < 0:
        player.pos[1] = 0
    elif player.pos[1] > window_size[1] / grid_size[1] - 1:
        player.pos[1] = window_size[1] / grid_size[1] - 1

    # Randomly add a new obstacle
    if random.random() < 0.1:
        if random.random() < 0.5:
            # 50% chance of creating a wall
            obstacles.append(Wall((random.randint(0, window_size[0] // grid_size[0] - 1),
                                  random.randint(0, window_size[1] // grid_size[1] - 1)), grid_size))
        else:
            # 50% chance of creating a trap
            obstacles.append(Trap((random.randint(0, window_size[0] // grid_size[0] - 1),
                                  random.randint(0, window_size[1] // grid_size[1] - 1)), grid_size))

    # Draw the background
    screen.fill(bg_color)

    # Draw the obstacles
    for obstacle in obstacles:
        print(obstacle)
        obstacle.draw(screen)

    # Draw the player
    player.draw(screen)

    # Update the display
    pygame.display.flip()

    # Limit the FPS
    clock.tick(60)

# Quit Pygame
pygame.quit()
