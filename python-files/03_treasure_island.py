print("Welcome to Treasure Island!")
print('''
                   ~.
            Ya...___|__..ab.     .   .
             Y88b  \88b  \88b   (     )
              Y88b  :88b  :88b   `.oo'
              :888  |888  |888  ( (`-'
     .---.    d88P  ;88P  ;88P   `.`.
    / .-._)  d8P-"""|"""'-Y8P      `.`.
   ( (`._) .-.  .-. |.-.  .-.  .-.   ) )
    \ `---( O )( O )( O )( O )( O )-' /
     `.    `-'  `-'  `-'  `-'  `-'  .' CJ
       `---------------------------
       ''')
user_input = input("Left or Right?\n").lower()

if user_input == "left":
    user_input = input("Swim or Wait?\n").lower()
    if user_input == "wait":
        user_input = input("Which door? (Yellow, Red, Blue)\n").lower()
        if user_input == "yellow":
            print("You win!")
        elif user_input == "red":
            print("You got burned by fire!")
        elif user_input == "blue":
            print("You drowned!")
        else:
            print("Game over!")
    else:
        print("You got attacked by a piranhas, game over!")
else:
    print("You fell into a hole, game over!")
