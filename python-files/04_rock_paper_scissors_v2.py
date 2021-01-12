from random import choice

separator = "--------------------------------------------------"
answers = ("Rock", "Paper", "Scissors")
possible_answers = tuple(i[0].lower() for i in answers)
exit_key = "q"
target_score = 3
is_playing = True


def check_quit(player_input):
    if player_input == exit_key:
        quit()


def reset_game():
    print(f"----- First one to win {target_score} games wins! -----")
    print(f"------- Type {exit_key.upper()} at any time to exit -------")
    two_player_mode = ask_player_count()
    play(two_player_mode)


def choose_answer(player):
    while True:
        answer = input(f"Player {player}: ").lower().strip()
        check_quit(answer)
        if answer[0] in possible_answers:
            return answer[0]
        print("That's not a valid option! Try again.")


def ask_player_count():
    while True:
        answer = input("Do you want to play against the computer? ").lower().strip()
        check_quit(answer)
        if answer[0] == "y":
            return False
        elif answer[0] == "n":
            return True
        print("That's not a valid option! Try again.")


def determine_winner(player1, player2, score):
    control_index = possible_answers.index(player1)
    print(f"Player One: {answers[possible_answers.index(player1)]}\n"
          f"Player Two: {answers[possible_answers.index(player2)]}")
    if player1 == player2:
        print("It's a tie!")
    elif player2 == possible_answers[(control_index + 2) % 3]:  # Simplified version of logic by Sora no Tenshi
        print("Player 1 Wins!")
        score["Player 1"] += 1
    else:
        print("Player 2 Wins!")
        score["Player 2"] += 1
    print(f"Score: {score['Player 1']} - {score['Player 2']}")
    print(separator)


def play(multiplayer):
    score = {"Player 1": 0, "Player 2": 0}
    while score["Player 1"] < target_score and score["Player 2"] < target_score:
        player_one = choose_answer("One")
        print(separator)
        if multiplayer:
            player_two = choose_answer("Two")
            print(separator)
        else:
            player_two = choice(possible_answers)
        determine_winner(player_one, player_two, score)

    if score["Player 1"] == target_score:
        print("Player 1 is the overall winner!")
    else:
        print("Player 2 is the overall winner!")

    while True:
        play_again = input("Do you want to play again? ").lower().strip()
        check_quit(play_again)
        if play_again[0] == "y":
            break
        elif play_again[0] == "n":
            print(separator)
            print("Thank you for playing!")
            print(separator)
            quit()
        print("That's not a valid option!")
    reset_game()


reset_game()
