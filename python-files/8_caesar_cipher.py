import string

alphabet = string.ascii_lowercase
numbers = string.digits
print("Welcome to caesar's lounge!")
mode = input("Which mode do you want me to run on? (full/custom)\n").lower().strip()
message = input("Type the message to rotate: ").lower().strip()

if len((set(message) & set(numbers))) > 0:
    rotate_numbers = input("Do you wish to encrypt numbers as well? [Not recommended if the message isn't only numbers]"
                           " (yes/no)\n").lower().strip()
    if rotate_numbers[0] == "y":
        rotate_numbers = True
    elif rotate_numbers[0] == "n":
        rotate_numbers = False
    else:
        print("Invalid option, using 'no' as default.")
        rotate_numbers = False


def rotate(msg, times):
    new_msg = []
    for char in msg:
        if char in alphabet:
            index = alphabet.index(char)
            new_msg.append(alphabet[(index + times) % len(alphabet)])
        elif char in numbers and rotate_numbers:
            index = numbers.index(char)
            new_msg.append(numbers[(index + times) % len(numbers)])
        else:
            new_msg.append(char)
    return "".join(new_msg)


if mode[0] == 'f':
    for i in range(len(alphabet)):
        print(f"ROT-{i}: {rotate(message, i)}")

elif mode[0] == 'c':
    custom_mode = input("Do you want to encrypt or decrypt? ").lower().strip()

    rot_times = 13
    # noinspection PyBroadException
    try:
        rot_times = int(input("Type the number of digits to shift: ")) % len(alphabet)
    except Exception:
        print("Not a valid input, using 13 as default.")

    if custom_mode[0] == 'e':
        print(f"ROT-{rot_times}: {rotate(message, rot_times)}")
    elif custom_mode[0] == 'd':
        print(f"ROT-{rot_times}: {rotate(message, -rot_times)}")
    else:
        print("Invalid option, encrypting as default.")
        print(f"ROT-{rot_times}: {rotate(message, rot_times)}")
