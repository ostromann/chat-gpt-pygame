import pygame


class Platform:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self, screen):
        # Draw the platform
        pygame.draw.rect(screen, self.color, pygame.Rect(
            self.x, self.y, self.width, self.height))
