from colorize import colorize
import json

# ----------------------------------------------------------------------------------------------------

machine_resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}
coin_values = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickels": 0.05,
    "pennies": 0.01
}

# ----------------------------------------------------------------------------------------------------

with open("drinks.json") as file:
    drinks = json.load(file)

# ----------------------------------------------------------------------------------------------------


def report():
    [print(colorize(f"{resource}: {machine_resources.get(resource)}", "yellow")) for resource in machine_resources]


# ----------------------------------------------------------------------------------------------------

def make_coffee(coffee):
    ingredients = coffee.get("ingredients")
    for ingredient in ingredients:
        machine_resources[ingredient] -= ingredients.get(ingredient)


# ----------------------------------------------------------------------------------------------------


def process_transaction(coffee, cost):
    print("Thank you for your purchase! here is your coffee: [Coffee Here]")
    make_coffee(coffee)
    machine_resources["money"] += cost


# ----------------------------------------------------------------------------------------------------


def validate_coins(user_coins, coffee):
    total_credit = round(sum([user_coins.get(coin) * coin_values.get(coin) for coin in user_coins]), 2)
    cost = coffee.get("cost")
    print(f"Your credit is: {colorize(f'${total_credit}', 'green')}")
    print(f"This beverage costs {colorize(f'${cost}', 'green')}")
    if total_credit == cost:
        process_transaction(coffee, cost)
        prompt()
    elif total_credit > cost:
        process_transaction(coffee, cost)
        print(f"Here's your change: {colorize(f'${total_credit - cost}', 'green')}")
        prompt()
    else:
        print("Not enough money for this purchase!")
        print(f"Here's your refund: {colorize(f'${total_credit}', 'red')}")
        prompt()


# ----------------------------------------------------------------------------------------------------


def ask_coins():
    total_coins = dict()

    for coin in coin_values:
        while True:
            user_input = input(f"How many {coin}? ").strip()
            try:
                total_coins.update({coin: int(user_input)})
                break
            except ValueError:
                print("That's not a valid number")

    return total_coins


# ----------------------------------------------------------------------------------------------------


def dispense(coffee):
    # This checks if the machine has all the required amounts of ingredients left
    coffee = drinks.get(coffee)
    ingredients = coffee.get("ingredients")
    can_dispense = all([ingredients.get(ingredient) <= machine_resources.get(ingredient) for ingredient in ingredients])
    if can_dispense:
        user_coins = ask_coins()
        validate_coins(user_coins, coffee)
    else:
        print(colorize("Machine out of resources for that coffee!", "red"))


# ----------------------------------------------------------------------------------------------------

def prompt():
    print(f"What would you like? {colorize('(espresso/latte/cappuccino)', 'cyan')}: ", end="")
    user_input = input().lower().strip()

    if user_input == 'off':
        quit()
    elif user_input == 'report':
        report()
        prompt()
    elif user_input in drinks:
        dispense(user_input)
        prompt()
    else:
        print("That's not a valid coffee!")
        prompt()


# ----------------------------------------------------------------------------------------------------

prompt()
