import pygame


class Input:
    def __init__(self):
        self.left = False
        self.right = False
        self.up = False
        self.down = False

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.left = True
                elif event.key == pygame.K_RIGHT:
                    self.right = True
                elif event.key == pygame.K_UP:
                    self.up = True
                elif event.key == pygame.K_DOWN:
                    self.down = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.left = False
                elif event.key == pygame.K_RIGHT:
                    self.right = False
                elif event.key == pygame.K_UP:
                    self.up = False
                elif event.key == pygame.K_DOWN:
                    self.down = False

        return True
