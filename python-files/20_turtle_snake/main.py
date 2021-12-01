from math import floor
from turtle import Screen
from scoreboard import Scoreboard
from snake import Snake
from food import Food
from time import sleep, time

WIDTH, HEIGHT = 500, 500
BG_COLOR, SNAKE_COLOR = 'black', 'white'
SPAWN_INTERVAL = 5


def exit_turtle():
    global playing
    playing = False
    screen.bye()


def game_over():
    screen.onkeypress(exit_turtle, "Return")
    snake.hide()
    food.hide()
    scoreboard.hide()
    scoreboard.game_over()
    screen.update()


def check_walls():
    if abs(snake.head.xcor()) > WIDTH // 2 or abs(snake.head.ycor()) > HEIGHT // 2:
        global playing
        playing = False


def play():
    next_spawn = floor(time())
    while playing:
        if floor(time()) >= next_spawn:
            next_spawn += SPAWN_INTERVAL
        snake.move()
        if snake.head.distance(food) < 10:
            scoreboard.increase_score()
            snake.add_segment()
            food.reposition(unavailable_spaces=snake.body())
        screen.update()
        check_walls()
        sleep(0.1)
    game_over()


# Canvas Setup
screen = Screen()
screen.setup(WIDTH-4, HEIGHT-18)
screen.bgcolor(BG_COLOR)
screen.title("Snake")
screen.tracer(0)

# Game Setup
snake = Snake(game_over, color=SNAKE_COLOR)
scoreboard = Scoreboard(x=0, y=HEIGHT//3, msg='Score: ', color='blue')
food = Food(WIDTH, HEIGHT)
playing = True

# Input Setup
screen.onkeypress(exit_turtle, "Escape")
screen.onkeypress(lambda: snake.change_direction(0), "Right")
screen.onkeypress(lambda: snake.change_direction(90), "Up")
screen.onkeypress(lambda: snake.change_direction(180), "Left")
screen.onkeypress(lambda: snake.change_direction(270), "Down")
screen.listen()

play()
screen.mainloop()
