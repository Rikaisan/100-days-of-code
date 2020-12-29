from random import choice
import art

# words = ("Water", "Zombie", "Teacher", "Bartender", "Audio Mixer", "Jupiter")
with open("words.txt") as file:
    lines = file.readlines()
    words = [word[:-1] for word in lines]
    del lines
print("\n----------------------------------------\n")
print(f"Imported {len(words)} words!")
print("Type 'quit' at any time to quit!")
print("\n----------------------------------------\n")
word = list(choice(words).lower())
word_set = set(word)

guesses = set()
lives = 6

if word.count(" ") >= 1:  # if the word has a space it gets added automatically to the guessed characters
    guesses.add(" ")


def generate_game_text():
    """This function turns the word into dashes and places the letter if it has been guessed"""
    global word
    global word_set
    filtered_list = [f"{letter} " if letter in guesses else "_ " for letter in word if letter in word_set]
    print("\n" + "".join(filtered_list))


def guess(guess_str):
    """This function manages the user guess and the guesses set"""
    if guess_str in guesses:
        print("You already guessed that one!")
        return True
    if guess_str in word_set:
        guesses.add(guess_str)
        return True
    else:
        return False


def print_man():
    """This function prints the hanging man"""
    print(art.stages[lives])


# This code only runs the first time the game loads
print(art.logo)
print_man()

while True:
    generate_game_text()
    user_guess = input("Enter your guess: ").lower().strip()

    if user_guess == "quit":  # Just in case the user wants to quit or guess a full word
        break
    elif user_guess == ''.join(word):
        print("You win!")
        break

# Checks if the user guess is correct and then proceeds with the logic
    guess_state = guess(user_guess)
    if guess_state:
        if len(guesses) == len(word_set):
            generate_game_text()
            print("You win!")
            break
        print_man()
    else:
        lives -= 1
        print_man()
    if lives <= 0:
        print("You lost!")
        print(f"The word was: {''.join(word)}")
        break
