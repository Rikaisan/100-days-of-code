from turtle import Turtle, Screen
from random import randint

colors = ["red", "blue", "green", "purple", "orange"]
screen = Screen()
screen.setup(width=800, height=600)
height = screen.screensize()[1] * 2
width = screen.screensize()[0] * 2
start_pos_x = -(width / 2) + 50
finish_line = width // 2 - 25
turtles = []


for item in colors:
    turtle = Turtle("turtle")
    turtle.color(item)
    turtle.penup()
    turtles.append([item, turtle])
    del turtle

number_of_turtles = len(turtles)
turtle_spacing = height / (number_of_turtles + 1)

for i in range(number_of_turtles):
    turtles[i][1].setpos(start_pos_x, -(height // 2) + turtle_spacing * (i + 1))

user_bet = screen.textinput("Place a bet", f"Options: {', '.join(colors)}").lower().strip()


def race():
    while True:
        for racer in turtles:
            if racer[1].xcor() < finish_line:
                racer[1].forward(randint(1, 10))
                if racer[1].xcor() >= finish_line:
                    return racer[0]


winner = race()
print(f"Winner is: {winner}")
if user_bet == winner:
    print("You win the bet!")
else:
    print("You lost the bet!")

screen.exitonclick()
