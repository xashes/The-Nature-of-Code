import arcade
import random

class Entity(arcade.SpriteCircle):
    def __init__(self, radius: int, color: arcade.Color, soft: bool = False):
        super().__init__(radius, color, soft)

    def walk(self) -> None:
        self.change_x = random.gauss(0, 5)
        self.change_y = random.gauss(0, 5)

    def on_update(self, delta_time: float = 1 / 60):
        self.walk()