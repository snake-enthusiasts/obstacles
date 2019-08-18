import sys
import pygame
from settings import Settings
from obstacle import Obstacle
from finish import Finish
from ship import Ship

class AlienInvasion(object):

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        # Make the Obstacles & Finish
        self.obstacles = pygame.sprite.Group()
        self._create_set_of_obstacles()
        self.finish = Finish(self)
        self.ship = Ship(self)


    def runGame(self):

        while True:
            self._check_events()
            self.ship.update()

            self._update_screen()


    def _check_events(self):
        """Responds to keyboard and mouse events"""
        # funkcja get() zwraca listę zdarzeń, które miały miejsce od czasu jej poprzedniego wywołania
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                # self._check_play_button(mouse_pos) <===================

    def _check_keydown_events(self, event):
        """Respond to keypresses"""
        if event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            # self._fire_bullet() <===================
            sys.exit()

    def _check_keyup_events(self, event):
        """Respond to key releases"""
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _update_screen(self):
        """Update images on the screen and flip to the new screen"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        self.finish.blitme()
        """
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        """

        # Draw the score information.
        # self.sb.show_score()

        # Draw the play button if the game is inactive.
        # if not self.stats.game_active:
        #    self.play_button.draw_button()
        self.obstacles.draw(self.screen)

        # Make the most recently drawn screen visible.
        pygame.display.flip()

    def _create_set_of_obstacles(self):
        """Create the set of obstacles"""
        obstacle = Obstacle(self)
        obstacle_width, obstacle_height = obstacle.rect.size
        available_space_x = self.settings.screen_width - (2 * obstacle_width)
        number_obstacles_x = available_space_x // (2 * obstacle_width)

        # Create the full set of obstacles
        for row_number in range(1, 4):
            # Create the full row of obstacles
            for obstacle_number in range(1, 4):
                self._create_obstacle(obstacle_number, row_number)

    def _create_obstacle(self, obstacle_number, row_number):
        """Create an obstacle and place it in the row"""
        obstacle = Obstacle(self)
        obstacle_width, obstacle_height = obstacle.rect.size

        # There are supposed to be a set 3x3 of obstacles
        # ... and we just hope that the screen is big enough ;)
        obstacle.rect.centerx = self.settings.screen_width/4 * obstacle_number
        obstacle.rect.centery = self.settings.screen_height/4 * row_number
        self.obstacles.add(obstacle)


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.runGame()
