from turtle import Turtle
from random import randint


class Food(Turtle):
    def __init__(self, width: int, height: int, color='red'):
        super().__init__()
        self.color(color)
        self.shape("circle")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.penup()
        self._limits = ((width // 2 - 20) // 20, (height // 2 - 20) // 20)
        self.reposition()

    def reposition(self, unavailable_spaces: list = None):
        old_pos = self.pos()
        invalid = False if not unavailable_spaces else any(self.distance(item) < 20 for item in unavailable_spaces)
        while self.pos() == old_pos or invalid:
            x_pos = 20 * randint(-self._limits[0], self._limits[0])
            y_pos = 20 * randint(-self._limits[0], self._limits[1])
            self.setpos(x_pos, y_pos)
            invalid = False if not unavailable_spaces else any(self.distance(item) < 20 for item in unavailable_spaces)

    def hide(self):
        self.hideturtle()
