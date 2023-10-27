import arcade

from .config import *


class Flappy(arcade.Sprite):
    def __init__(self, pipes):
        super().__init__(ASSETS / 'images/yellowbird-midflap.png')

        self.pipes = pipes
        self.center_x = WIDTH / 2
        self.center_y = HEIGHT / 2
        self.vy = 0

    def on_update(self, delta_time: float = 1 / 60):
        self.vy += GRAVITY
        self.center_y += self.vy

        # check borders
        if self.bottom < 0 or self.top > HEIGHT:
            print('>> game over')
            quit()

        # check collisions with pipes
        if self.collides_with_list(self.pipes):
            print('>> you have died')
            quit()

    def flap(self):
        self.vy = KICK
