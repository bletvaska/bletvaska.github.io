#!/usr/bin/env python
import random

import arcade

from .pipe import Pipe
from .config import *
from .flappy import Flappy


class FlappyBird(arcade.Window):
    def __init__(self):
        super().__init__(WIDTH, HEIGHT, TITLE)

        self.sprites = None
        self.flappy = None
        self.background = None
        self.pipes = None
        self.speed = 1

    def setup(self):
        self.background = arcade.load_texture(ASSETS / 'images/background-day.png')
        self.sprites = arcade.SpriteList()
        self.pipes = arcade.SpriteList()

        # spawn flappy
        self.flappy = Flappy(self.pipes)
        self.sprites.append(self.flappy)

        self._spawn_pipes()

    def _spawn_pipes(self, speed=1):
        # spawn pipes
        spawn_point = random.randint(HEIGHT / 2 - 140, HEIGHT / 2 + 140)
        upper_pipe = Pipe(ASSETS / 'images/pipe-green.png', speed, flipped_vertically=True)
        upper_pipe.bottom = spawn_point + GAP / 2
        lower_pipe = Pipe(ASSETS / 'images/pipe-green.png', speed)
        lower_pipe.top = spawn_point - GAP / 2
        self.pipes.append(upper_pipe)
        self.pipes.append(lower_pipe)

    def on_key_press(self, symbol, modificators):
        if symbol == arcade.key.Q and modificators & arcade.key.MOD_CTRL:
            print('(c) Cretated by mirek 2023')
            quit()

        if symbol == arcade.key.SPACE:
            self.flappy.flap()

    def on_draw(self):
        arcade.draw_texture_rectangle(WIDTH // 2, HEIGHT // 2, WIDTH, HEIGHT, self.background)
        self.sprites.draw()
        self.pipes.draw()

    def on_update(self, dt):
        self.sprites.on_update(dt)
        self.pipes.on_update(dt)

        if len(self.pipes) == 0:
            self.speed += 0.1
            self._spawn_pipes(self.speed)


def main():
    game = FlappyBird()
    game.setup()
    arcade.run()


if __name__ == '__main__':
    main()
