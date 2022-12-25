import pygame


class Player:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.velocity = [0, 0]

    def update(self):
        # Update the player position
        self.x += self.velocity[0]
        self.y += self.velocity[1]

    def draw(self, screen):
        # Draw the player
        pygame.draw.rect(screen, self.color, pygame.Rect(
            self.x, self.y, self.width, self.height))
