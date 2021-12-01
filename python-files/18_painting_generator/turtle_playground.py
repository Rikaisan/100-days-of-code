from turtle import Turtle, Screen
from random import choice

turtle = Turtle()
turtle.shape("turtle")
colors = ["aquamarine", "#B22222", "magenta", "medium slate blue", "blue", "#008B8B", "red", "black", "green", "orange"]
turtle.speed(0)
screen = Screen()


def draw_square():
    for _ in range(4):
        turtle.forward(100)
        turtle.right(90)


def draw_dotted():
    for _ in range(20):
        turtle.forward(10)
        turtle.penup()
        turtle.forward(10)
        turtle.pendown()


def draw_shape(sides):
    angle = 360/sides
    for side in range(sides):
        turtle.forward(20)
        turtle.right(angle)


def random_path(times):
    degrees = [0, 90, 180, 270]
    turtle.pensize(10)
    for time in range(times):
        turtle.color(choice(colors))
        direction = choice(degrees)
        turtle.forward(20)
        turtle.seth(direction)


def spiro(degrees=5):
    for time in range(360//degrees):
        # turtle.color(choice(colors))
        turtle.circle(100)
        turtle.left(degrees)


# for i in range(3, 10):
#     turtle.color(choice(colors))
#     draw_shape(i)

# random_path(250)
spiro(3)

screen.exitonclick()
