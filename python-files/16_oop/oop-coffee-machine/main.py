from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from colorize import colorize

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


def prompt():
    print("What do you want to drink?")
    print(f"Menu: {colorize(menu.get_items(), 'cyan')}")
    user_input = input().lower().strip()

    if user_input == 'off':
        quit()
    elif user_input == 'report':
        coffee_maker.report()
        money_machine.report()

    drink = menu.find_drink(user_input)
    if drink and coffee_maker.is_resource_sufficient(drink):
        if money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
    prompt()


prompt()
