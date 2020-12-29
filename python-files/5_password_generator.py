import random
import string


def set_total(last=False):
    global total_length
    if last:
        total = total_length
        total_length -= total
        return total
    total = random.randint(1, total_length)
    total_length -= total
    return total


def generate_password(letters, symbols, numbers):
    password = []
    for i in range(letters):
        password.append(random.choice(string.ascii_letters))

    for i in range(symbols):
        password.append(random.choice(string.punctuation))

    for i in range(numbers):
        password.append(random.choice(string.digits))

    random.shuffle(password)
    password = "".join(password)
    return password


while True:
    mode = input("Which mode do you want to use to generate passwords? (auto/manual/quit)\n").lower()
    if mode == "quit":
        break
    elif mode == "manual":
        num_of_letters = int(input("How many letters do you want?\n"))
        num_of_symbols = int(input("How many symbols do you want?\n"))
        num_of_numbers = int(input("How many numbers do you want?\n"))

        print(generate_password(num_of_letters, num_of_symbols, num_of_numbers))
        break
    elif mode == "auto":
        total_length = int(input("How many characters do you want your password to be?\n"))
        num_of_letters = set_total()
        num_of_symbols = set_total()
        num_of_numbers = set_total(True)

        print(generate_password(num_of_letters, num_of_symbols, num_of_numbers))
        break
    else:
        print("Invalid command!")
