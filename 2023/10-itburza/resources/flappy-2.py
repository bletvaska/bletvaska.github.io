from time import sleep

import arcade

GRAVITY = -0.3
KICK = 6.5
WIDTH = 288
HEIGHT = 512
TITLE = 'flap.py'


class Flappy(arcade.Window):
    def __init__(self):
        super().__init__(WIDTH, HEIGHT, TITLE)

        self.background = arcade.load_texture('assets/images/background.png')

        self.flappy = arcade.Sprite('assets/images/flappy.png')
        self.flappy.center_x = self.width / 2
        self.flappy.center_y = self.height / 2
        self.flappy.vy = 0

        self.hit_sound = arcade.load_sound('assets/sounds/hit.wav')
        self.wing_sound = arcade.load_sound('assets/sounds/wing.wav')
        self.die_sound = arcade.load_sound('assets/sounds/die.wav')

        self.pipe_lower = arcade.Sprite('assets/images/pipe.png')
        self.pipe_upper = arcade.Sprite('assets/images/pipe.png', flipped_vertically=True)
        self.pipe_upper.left = self.width
        self.pipe_upper.bottom = self.height / 2

    def on_update(self, delta_time: float):
        # flappy
        self.flappy.vy += GRAVITY
        self.flappy.center_y += self.flappy.vy

        if self.flappy.bottom <= 0 or self.flappy.top >= self.height:
            self.hit_sound.play()
            print('>> si mrtvy. je mi to luto. ale taky je zivot.')
            sleep(10)
            arcade.close_window()

        # pipes
        self.pipe_upper.center_x -= 1
        if self.pipe_upper.right <= 0:
            self.pipe_upper.left = self.width

        # collision detection
        if self.flappy.collides_with_sprite(self.pipe_upper) is True:
            self.die_sound.play()
            print('>> ta trupku neprerazis. si mrtvy')
            sleep(10)
            arcade.close_window()

    def on_draw(self):
        # self.clear()
        arcade.draw_texture_rectangle(
            self.width / 2, self.height / 2,
            self.background.width, self.background.height,
            self.background
        )
        self.pipe_upper.draw()
        # self.pipe_lower.draw()
        self.flappy.draw()

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.SPACE:
            self.wing_sound.play()
            self.flappy.vy = KICK


game = Flappy()
arcade.run()
