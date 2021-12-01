from turtle import Turtle, Screen
from random import choice
# import colorgram
import json

turtle = Turtle()
turtle.penup()
turtle.width(20)
turtle.shape("circle")
turtle.hideturtle()
turtle.speed(0)
screen = Screen()
screen.colormode(255)

with open("colors.json") as file:
    # image_colors = colorgram.extract("painting.jpg", 14)
    # colors = [(color.rgb[0], color.rgb[1], color.rgb[2]) for color in image_colors]
    # json.dump(colors, file, indent=4)
    colors = json.load(file)


def set_color():
    color = choice(colors)
    turtle.color(color)


def paint(num):
    turtle.setpos(-300, -300)
    for n in range(num):
        for i in range(num):
            set_color()
            turtle.forward(50)
            turtle.stamp()
        turtle.left(90)
        turtle.forward(50)
        turtle.right(90)
        turtle.setpos(-300, turtle.ycor())


paint(10)
screen.exitonclick()
