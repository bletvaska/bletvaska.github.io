#!/usr/bin/env python
from pathlib import Path
import arcade

from .config import *
from .flappy import Flappy

class FlappyBird(arcade.Window):
    def __init__(self):
        super().__init__(WIDTH, HEIGHT, TITLE)

        self.sprites = None
        self.flappy = None

    def setup(self):
        self.sprites = arcade.SpriteList()

        self.flappy = Flappy()
        self.sprites.append(self.flappy)
        self.background = arcade.load_texture(ASSETS / 'background-day.png')

    def on_key_press(self, symbol, modificators):
        if symbol == arcade.key.Q and modificators & arcade.key.MOD_CTRL:
            print('(c) Cretated by mirek 2023')
            quit()

        if symbol == arcade.key.SPACE:
            self.flappy.flap()

    def on_draw(self):
        arcade.draw_texture_rectangle(WIDTH // 2, HEIGHT // 2, WIDTH, HEIGHT, self.background)
        self.sprites.draw()

    def on_update(self, dt):
        self.sprites.on_update(dt)

def main():
    game = FlappyBird()
    game.setup()
    arcade.run()

if __name__ == '__main__':
    main()
