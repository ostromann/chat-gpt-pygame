import pygame


class Player:
    def __init__(self, pos, grid_size, color):
        self.pos = list(pos)  # Change pos to a list
        self.grid_size = grid_size
        self.color = color
        self.velocity = [0, 0]

    def update(self):
        # Update the player position
        self.pos[0] += self.velocity[0]
        self.pos[1] += self.velocity[1]

    def draw(self, screen):
        # Calculate the player's screen position
        x = self.pos[0] * self.grid_size[0]
        y = self.pos[1] * self.grid_size[1]

        # Draw the player
        pygame.draw.rect(screen, self.color, pygame.Rect(
            x, y, self.grid_size[0], self.grid_size[1]))
