from time import sleep

import arcade

from .config import *


class Flappy(arcade.Sprite):
    def __init__(self, pipes):
        super().__init__(ASSETS / 'images/yellowbird-midflap.png')

        self.die_sound = arcade.load_sound(ASSETS / "sounds/die.wav")
        self.hit_sound = arcade.load_sound(ASSETS / "sounds/hit.wav")
        self.wing_sound = arcade.load_sound(ASSETS / "sounds/wing.wav")

        self.pipes = pipes
        self.center_x = WIDTH / 2
        self.center_y = HEIGHT / 2
        self.vy = 0

    def on_update(self, delta_time: float = 1 / 60):
        self.vy += GRAVITY
        self.center_y += self.vy

        # check borders
        if self.bottom < 0 or self.top > HEIGHT:
            self.hit_sound.play()
            print('>> game over')
            sleep(1)
            arcade.close_window()

        # check collisions with pipes
        if self.collides_with_list(self.pipes):
            self.hit_sound.play()
            print('>> you have died')
            sleep(1)
            arcade.close_window()

    def flap(self):
        self.wing_sound.play()
        self.vy = KICK
