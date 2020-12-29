# Paper wins to Rock
# Rock wins to Scissors
# Scissors wins to Paper
# Else: Draw
games_to_win = 3
player1_score = 0
player2_score = 0
mode = input("Do you wish to play against AI? [y/n]\n").lower()
print(f"Playing to {games_to_win} wins")
while not (player1_score >= games_to_win or player2_score >= games_to_win):
    if mode == 'y':
        import random
        player1 = input("Enter your choice:\n").lower().strip()
        ai = random.choice(["rock", "paper", "scissors"])
        if player1 and ai:
            if player1[0] == ai[0]:
                print(f"Player 2[AI] picks {ai}, it's a draw!")
            elif ((player1[0] == "p" and ai[0] == "r") or
                  (player1[0] == "r" and ai[0] == "s") or
                  (player1[0] == "s" and ai[0] == "p")):
                print(f"Player 2[AI] picks {ai}, you win!")
                player1_score += 1
                print(f"\nScore:\n  Player 1: {player1_score}\n  Player 2[AI]: {player2_score}\n")
            else:
                print(f"Player 2[AI] picks {ai}, AI wins!")
                player2_score += 1
                print(f"\nScore:\n  Player 1: {player1_score}\n  Player 2[AI]: {player2_score}\n")
        else:
            print("Invalid input!")
    elif mode == 'n':
        player1 = input("Enter Player 1 choice:\n").lower().strip()
        player2 = input("Enter Player 2 choice:\n").lower().strip()
        if player1 and player2:
            if player1[0] == player2[0]:
                print("Draw!")
            elif ((player1[0] == "p" and player2[0] == "r") or
                  (player1[0] == "r" and player2[0] == "s") or
                  (player1[0] == "s" and player2[0] == "p")):
                print("Player 1 wins!")
                player1_score += 1
                print(f"\nScore:\n  Player 1: {player1_score}\n  Player 2: {player2_score}\n")
            else:
                print("Player 2 wins!")
                player2_score += 1
                print(f"\nScore:\n  Player 1: {player1_score}\n  Player 2: {player2_score}\n")
        else:
            print("Invalid input!")
    else:
        print("Invalid input!")

if player1_score > player2_score:
    print("\nGame ended, Player 1 Wins!")
else:
    print("\nGame ended, Player 2 Wins!")
