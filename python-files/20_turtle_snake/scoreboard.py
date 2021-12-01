from turtle import Turtle
import os

FONT = ("Courier", 24, "bold")
ALIGNMENT = "center"
score_file = 'scores.txt'


def get_high_score():
    if os.path.isfile(score_file):
        with open(score_file) as file:
            return int(file.read())
    return 0


def save_high_score(score: int):
    with open(score_file, 'w') as file:
        file.write(str(score))


class Scoreboard(Turtle):
    def __init__(self, x, y, msg='', color='black'):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.setpos(x, y)
        self.color(color)
        self.msg = msg
        self.score = 0
        self.update()
        self.high_score = get_high_score()

    def update(self):
        self.clear()
        self.write(self.msg + str(self.score), False, ALIGNMENT, FONT)

    def increase_score(self, amount=1):
        self.score += amount
        self.update()

    def hide(self):
        self.clear()

    def game_over(self):
        if self.score > self.high_score:
            self.high_score = self.score
            save_high_score(self.high_score)
        self.setpos(0, 48)
        self.write("Game Over", False, ALIGNMENT, FONT)
        self.setpos(0, self.pos()[1] - (FONT[1] + 10))
        self.write("High score: " + str(self.high_score), False, ALIGNMENT, FONT)
        self.setpos(0, self.pos()[1] - (FONT[1] + 10))
        self.write("Score: " + str(self.score), False, ALIGNMENT, FONT)
        self.setpos(0, self.pos()[1] - (FONT[1] + 10))
        self.write("Press Enter to exit", False, ALIGNMENT, FONT)
