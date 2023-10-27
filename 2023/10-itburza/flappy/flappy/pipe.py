import arcade
from .config import WIDTH


class Pipe(arcade.Sprite):
    def __init__(self, filename, speed=1, *args, **kwargs):
        super().__init__(filename, *args, **kwargs)

        self.left = WIDTH
        self.speed = speed
        self.velocity = (-self.speed, 0)

    def on_update(self, delta_time: float = 1 / 60):
        super().update()

        if self.right < 0:
            self.remove_from_sprite_lists()
