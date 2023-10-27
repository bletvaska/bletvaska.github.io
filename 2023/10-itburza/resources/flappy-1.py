# https://codeshare.io/eVlKA4
from time import sleep

import arcade

GRAVITY = -0.3
KICK = 6.5


class Flappy(arcade.Window):
    def __init__(self):
        super().__init__(400, 600, 'Flap.py')

        self.flappy = arcade.Sprite('assets/images/flappy.png')
        self.flappy.center_x = self.width / 2
        self.flappy.center_y = self.height / 2
        self.flappy.vy = 0

        self.flap_sound = arcade.load_sound('assets/sounds/wing.wav')
        self.hit_sound = arcade.load_sound('assets/sounds/hit.wav')
        self.die_sound = arcade.load_sound('assets/sounds/die.wav')

        self.pipe = arcade.Sprite('assets/images/pipe.png')
        self.pipe.top = self.height / 2
        self.pipe.left = self.width

    def on_update(self, delta_time: float):
        self.flappy.vy += GRAVITY
        self.flappy.center_y += self.flappy.vy

        if self.flappy.bottom < 0 or self.flappy.top > self.height:
            self.hit_sound.play()
            print('>> you are dead flappy. sorry')
            sleep(10)
            arcade.close_window()

        self.pipe.center_x += -1

        if self.flappy.collides_with_sprite(self.pipe) is True:
            self.die_sound.play()
            print('>> ta si nabural do pajpy. sorry')
            sleep(10)
            arcade.close_window()

    def on_draw(self):
        self.clear()
        self.flappy.draw()
        self.pipe.draw()

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.SPACE:
            self.flap_sound.play()
            self.flappy.vy = KICK


game = Flappy()
arcade.run()
