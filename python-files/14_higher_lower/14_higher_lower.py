# There was no challenge for day 13 :(
import json
from random import choice
from colorize import colorize

# ----------------------------------------------------------------------------------------------------

bad_color = 'red'
name_color = 'cyan'
quit_color = 'magenta'
alert_color = 'magenta'
score_color = 'green'
option_color = 'yellow'
op1_key = 'a'
op2_key = 'b'
quit_key = 'q'
op1_badge = colorize(f'[{op1_key.upper()}]', option_color)
op2_badge = colorize(f'[{op2_key.upper()}]', option_color)
quit_badge = colorize(f'[{quit_key.upper()}]', quit_color)

# ----------------------------------------------------------------------------------------------------


with open("json_data.json") as file:
    data = json.load(file)


# ----------------------------------------------------------------------------------------------------


def determine_winner():
    if op1.get("follower_count") > op2.get("follower_count"):
        return op1_key
    else:
        return op2_key


# ----------------------------------------------------------------------------------------------------


def set_attributes():
    opt1_format = colorize(op1.get("name"), name_color)
    opt2_format = colorize(op2.get("name"), name_color)
    score_format = colorize(score, score_color)
    return opt1_format, opt2_format, score_format


# ----------------------------------------------------------------------------------------------------


def scroll_options():
    global op1, op2
    op1 = op2
    op2 = choice(data)
    data.pop(data.index(op2))


# ----------------------------------------------------------------------------------------------------

print(f"\nWelcome to Higher-Lower! You can leave at any time with {quit_badge}")
op1 = {}
op2 = choice(data)
data.pop(data.index(op2))
score = 0

# ----------------------------------------------------------------------------------------------------

while True:
    scroll_options()
    winner = determine_winner()

    op1_name, op2_name, score_badge = set_attributes()

    print(f"\nWho has more Instagram followers? Your score: {score_badge}")
    print(f"{op1_badge} {op1_name}, {op1.get('description')} from {op1.get('country')}")
    print(f"{op2_badge} {op2_name}, {op2.get('description')} from {op2.get('country')}")
    print(f"Type {op1_badge} or {op2_badge}: ", end="")

    user_input = input().lower().strip()
    if user_input == quit_key:
        print(f"\n{colorize('Bye Bye!', alert_color)} Score: {score_badge}")
        quit()
    if user_input == winner:
        score += 1
    else:
        print(f"\n{colorize('You lost!', bad_color)} Score: {score_badge}")
        quit()
