import arcade


class MyWindow(arcade.Window):

    def __init__(self, width, height, title):

        # Call the parent class's init function
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.ASH_GREY)

        self.ball_x = 50
        self.ball_y = 50

    def on_draw(self):
        """ Called whenever we need to draw the window. """
        arcade.start_render()

        arcade.draw_circle_filled(self.ball_x, self.ball_y, 15, arcade.color.AUBURN)

    def update(self, delta_time):
        """ Called to update our objects. Happens approximately 60 times per second."""
        self.ball_x += 1
        self.ball_y += 1

window = MyWindow(640, 480, "Drawing Example")

arcade.run()
