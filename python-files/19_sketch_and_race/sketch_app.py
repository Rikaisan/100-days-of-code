from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()
move_amount = 5
rotate_amount = 5


def move_forward():
    turtle.forward(move_amount)


def move_backwards():
    turtle.back(move_amount)


def rotate_left():
    turtle.left(rotate_amount)


def rotate_right():
    turtle.right(rotate_amount)


screen.listen()
screen.onkeypress(key="Up", fun=move_forward)
screen.onkeypress(key="Down", fun=move_backwards)
screen.onkeypress(key="Right", fun=rotate_right)
screen.onkeypress(key="Left", fun=rotate_left)
screen.onkeypress(key="c", fun=screen.reset)

screen.exitonclick()
