# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json
# Hurdle 4

def turn_right():
    turn_left()
    turn_left()
    turn_left()


wall_height = 0
while not at_goal():
    if wall_in_front():
        turn_left()
        move()
        turn_right()
        wall_height += 1
    elif front_is_clear():
        move()
        if wall_height > 0:
            turn_right()
            for times in range(wall_height):
                move()
            turn_left()
            wall_height = 0

# -------------------------------------------------------

def turn_right():
    turn_left()
    turn_left()
    turn_left()


while not at_goal():
    if wall_in_front():
        turn_left()
        if front_is_clear():
            move()
            turn_right()
        else:
            turn_left()
    elif front_is_clear():
        move()
        turn_right()

# ---------------------------------------------------------

def turn_right():
    turn_left()
    turn_left()
    turn_left()


while not at_goal():
    if is_facing_north() and wall_on_right():
        move()
    elif is_facing_north() and right_is_clear():
        turn_right()
        move()
        turn_right()
    elif wall_in_front() and wall_on_right():
        turn_left()
    elif front_is_clear():
        move()

# ---------------------------------------------------------
# MAZEEEEE

def turn_right():
    turn_left()
    turn_left()
    turn_left()


if front_is_clear():
    move()
    turn_left()
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear() and wall_on_right():
        move()
    elif wall_in_front() and wall_on_right():
        turn_left()