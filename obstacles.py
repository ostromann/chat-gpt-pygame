import abc
import pygame


class Obstacle(abc.ABC):
    def __init__(self, pos, grid_size):
        self.pos = pos
        self.grid_size = grid_size

    @abc.abstractmethod
    def draw(self, screen):
        pass


class Wall(Obstacle):
    def __init__(self, pos, grid_size):
        super().__init__(pos, grid_size)
        self.color = (0, 0, 0)

    def draw(self, screen):
        # Calculate the wall's screen position
        x = self.pos[0] * self.grid_size[0]
        y = self.pos[1] * self.grid_size[1]

        # Draw the wall
        pygame.draw.rect(screen, self.color, pygame.Rect(
            x, y, self.grid_size[0], self.grid_size[1]))


class Trap(Obstacle):
    def __init__(self, pos, grid_size):
        super().__init__(pos, grid_size)
        self.color = (255, 0, 0)

    def draw(self, screen):
        # Calculate the trap's screen position
        x = self.pos[0] * self.grid_size[0]
        y = self.pos[1] * self.grid_size[1]

        # Draw the trap
        pygame.draw.rect(screen, self.color, pygame.Rect(
            x, y, self.grid_size[0], self.grid_size[1]))
