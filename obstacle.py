import pygame
from pygame.sprite import Sprite

class Obstacle(Sprite):

    def __init__(self, ai_game):
        """Initialize obstacle"""
        super().__init__()
        self.screen = ai_game.screen
        """        self.screen_rect = self.screen.get_rect()

        # Set the dimension and properties of the Obstacle.
        self.width = int(self.screen_rect.width/10)
        self.height = int(self.screen_rect.height/10)
        self.button_color = (0, 255, 0)

        # Build the obstacle's rect object and center it
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        """
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        # Start each new alien near the top left of the screen.
        self.rect.x = 2 * self.rect.width
        self.rect.y = 2 * self.rect.width
        """
            def draw_obstacle(self):
                # Draw obstacle on the screen.
                self.screen.fill(self.button_color, self.rect)
        """
