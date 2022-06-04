"""
Platformer Game
"""
import arcade
from numpy import arange
import random

# Constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "Platformer"


# Constants used to scale our sprites from their original size

CHARACTER_SCALING = 1

TILE_SCALING = 0.5

class Walker(arcade.SpriteCircle):
    def __init__(self, radius: int, color: arcade.Color, soft: bool = False):
        super().__init__(radius, color, soft)

    def walk(self) -> None:
        self.center_x += random.gauss(0, 5)
        self.center_y += random.gauss(0, 5)

    def on_update(self, delta_time: float = 1 / 60):
        self.walk()


class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self):

        # Call the parent class and set up the window
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)


        # These are 'lists' that keep track of our sprites. Each sprite should

        # go into a list.
        self.scene = None

        self.physics_engine = None

        # Separate variable that holds the player sprite
        self.player_sprite = None

        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)


    def setup(self):

        """Set up the game here. Call this function to restart the game."""
        self.scene = arcade.Scene()

        self.scene.add_sprite_list('Walkers')
        self.scene.add_sprite_list('Walls', use_spatial_hash=True)

        # self.physics_engine = arcade.PymunkPhysicsEngine()

        # Set up the player, specifically placing it at these coordinates.

        image_source = ":resources:images/animated_characters/female_adventurer/femaleAdventurer_idle.png"

        for i in range(10):
            walker = Walker(10, arcade.color.FIREBRICK)
            walker.center_x = random.randrange(self.width)
            walker.center_y = random.randrange(self.height)
            self.scene.add_sprite('Walkers', walker)
            # self.physics_engine.add_sprite(walker)

        # Create the ground
        # This shows using a loop to place multiple sprites horizontally
        for x in range(0, 1250, 64):
            wall = arcade.Sprite(":resources:images/tiles/grassMid.png", TILE_SCALING)
            wall.center_x = x
            wall.center_y = 32
            self.scene.add_sprite("Walls", wall)


    def on_draw(self):
        """Render the screen."""

        # Clear the screen to the background color
        self.clear()

        # Draw our sprites
        self.scene.draw()

    def on_update(self, delta_time: float):
        # self.physics_engine.step()
        self.scene.on_update(delta_time, names=['Walkers'])


def main():
    """Main function"""
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()