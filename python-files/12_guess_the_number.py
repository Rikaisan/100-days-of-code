from random import randint
from colorama import init, Fore

init()

easy_attempts = 10
hard_attempts = 5
max_number = 100
cpu_number = randint(1, max_number)

print("\nWelcome to the number guesser game!")
print(f"I'm thinking of a number between {Fore.MAGENTA + '1' + Fore.WHITE} and "
      f"{Fore.MAGENTA + str(max_number) + Fore.WHITE}")
print(f"Choose a difficulty to start {Fore.YELLOW + '[Easy/Hard]' + Fore.WHITE}: ", end="")
mode = input().lower().strip()

if not mode:
    print(Fore.YELLOW + "Not a valid option, using easy as default" + Fore.WHITE)
    permitted_attempts = easy_attempts
else:
    if mode[0] == 'e':
        permitted_attempts = easy_attempts
    elif mode[0] == 'h':
        permitted_attempts = hard_attempts
    else:
        print(Fore.YELLOW + "Not a valid option, using easy as default" + Fore.WHITE)
        permitted_attempts = easy_attempts

guesses_left = permitted_attempts
while True:
    print(f"\nYou have {Fore.MAGENTA + str(guesses_left) + Fore.WHITE} attempts left")
    while True:
        print(f"Make a guess or type {Fore.RED + 'q' + Fore.WHITE} to quit: ", end="")
        user_guess = input().lower().strip()
        if user_guess == "q":
            print(Fore.CYAN + "Bye bye!!")
            quit()
        try:
            user_guess = int(user_guess)
            if user_guess < 0 or user_guess > max_number:
                raise UserWarning
            break
        except ValueError:
            print(Fore.YELLOW + "Please type a number!" + Fore.WHITE)
        except UserWarning:
            print(Fore.YELLOW + f"Please type a number between 1 and {max_number}!" + Fore.WHITE)

    if user_guess == cpu_number:
        guesses_left -= 1
        print(f"{Fore.GREEN}You win! It took you "
              f"{Fore.MAGENTA + str(permitted_attempts - guesses_left) + Fore.GREEN} attempts!")
        break
    guesses_left -= 1
    if guesses_left == 0:
        print(Fore.RED + f"You don't have any attempts left! My number was {Fore.MAGENTA + str(cpu_number)}")
        quit()

    if user_guess < cpu_number:
        print(Fore.GREEN + "My number is bigger!" + Fore.WHITE)
    else:
        print(Fore.RED + "My number is smaller!" + Fore.WHITE)
