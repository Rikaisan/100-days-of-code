import json
import data
from colorize import colorize

print(colorize("\nEnter the name of the variable to use: ", "magenta"), end="")
user_input = input()
data = getattr(data, user_input)

with open("data.json", "w") as file:
    json.dump(data, file, indent=4)

print(colorize("\nUpdated data file to:\n", "green"), colorize(data, "cyan"))