import pygame
from pygame.sprite import Sprite

class Finish(Sprite):
    """A class to let player finish this game"""

    def __init__(self, ai_game):
        """Initialize the finish and set its position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        self.rect.right = self.screen_rect.right
        self.rect.top = self.screen_rect.top

    def blitme(self):
        self.screen.blit(self.image, self.rect)
