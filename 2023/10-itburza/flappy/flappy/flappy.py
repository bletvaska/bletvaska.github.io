import arcade

from .config import *

GRAVITY = -0.3
KICK = 6.5


class Flappy(arcade.Sprite):
    def __init__(self):
        super().__init__(ASSETS / 'yellowbird-midflap.png')

        self.center_x = WIDTH / 2
        self.center_y = HEIGHT / 2
        self.vy = 0
        print(self.texture)
        print(self.textures)

    def on_update(self, dt):
        self.vy += GRAVITY
        self.center_y += self.vy

        # check borders
        if self.bottom < 0 or self.top > HEIGHT:
            print('>> game over')
            quit()

    def flap(self):
        self.vy = KICK

