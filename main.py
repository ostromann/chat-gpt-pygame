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

# Set the player properties
player_size = (50, 50)
player_color = (0, 0, 255)
player_pos = [100, 100]

# Set the platform properties
platform_width = 200
platform_height = 20
platform_color = (0, 255, 0)
platform_pos = [200, 300]

# Set the player movement variables
player_velocity = [0, 0]
gravity = 0.5

# Set the FPS clock
clock = pygame.time.Clock()

# Run the game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_velocity[0] = -5
            if event.key == pygame.K_RIGHT:
                player_velocity[0] = 5
            if event.key == pygame.K_UP:
                player_velocity[1] = -10
    # Update the player position
    player_pos[0] += player_velocity[0]
    player_pos[1] += player_velocity[1]
    # Apply gravity to the player
    player_velocity[1] += gravity

    # Check if the player is on a platform
    if (player_pos[1] + player_size[1] > platform_pos[1] and
        player_pos[0] + player_size[0] > platform_pos[0] and
            player_pos[0] < platform_pos[0] + platform_width):
        player_velocity[1] = 0
        player_pos[1] = platform_pos[1] - player_size[1]

    # Draw the background
    screen.fill(bg_color)

    # Draw the platform
    pygame.draw.rect(screen, platform_color, pygame.Rect(
        platform_pos[0], platform_pos[1], platform_width, platform_height))

    # Draw the player
    pygame.draw.rect(screen, player_color, pygame.Rect(
        player_pos[0], player_pos[1], player_size[0], player_size[1]))

    # Update the display
    pygame.display.flip()

    # Limit the FPS
    clock.tick(60)

# Quit Pygame
pygame.quit()
