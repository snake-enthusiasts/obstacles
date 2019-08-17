import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        self.obstacles = ai_game.obstacles


        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a decimal value for the ship's horizontal position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Movement flag
        self.moving_up = False
        self.moving_right = False
        self.moving_down = False
        self.moving_left = False

        self.collision_with_obstacle = False

    def update(self):
        """Update the ship's position based on the movement flag."""
        # Update the ship's x and y value, not the rect.
        x_temp = self.rect.x
        y_temp = self.rect.y
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0: # działa też self.screen_rect.left
            self.x -= self.settings.ship_speed

        self.rect.x = self.x
        self.rect.y = self.y

        # If there is no collision with obstace
        # update rect object from self.x and self.y.
        self.collision_with_obstacle = pygame.sprite.spritecollideany(self, self.obstacles)
        if not self.collision_with_obstacle:
            print("OK")
        else:
            self.rect.x = x_temp
            self.rect.y = y_temp

            self.x = float(self.rect.x)
            self.y = float(self.rect.y)
            print("Obstacle")
        """
            self.x = x_temp
            self.y = y_temp
            self.rect.x = self.x
            self.rect.y = self.y

            self.collision_with_obstacle = False

            self.moving_up = False
            self.moving_right = False
            self.moving_down = False
            self.moving_left = False
        """

    def blitme(self):
        self.screen.blit(self.image, self.rect)
