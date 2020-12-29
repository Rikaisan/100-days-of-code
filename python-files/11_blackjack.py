from random import choice
from time import sleep
from colorama import init, Fore

init()

deck_preset = ("A", *range(2, 11), "J", "Q", "K")
deck = [item for item in deck_preset for i in range(4)]
del deck_preset


class Card:
    special_names = ["A", "J", "Q", "K"]

    def __init__(self, name):
        if name == "A":
            self.name = str(name)
            self.value = 11
        elif name in Card.special_names:
            self.name = str(name)
            self.value = 10
        else:
            self.value = name
            self.name = str(name)

    def __repr__(self):
        if self.name in Card.special_names:
            return f"{self.name}({self.value})"
        else:
            return f"{self.name}"


def calculate_scores(player):
    return sum([card.value for card in player])


def validate_score(player):
    if calculate_scores(player) > 21:
        return True


def print_cards(player, method="spread", hide_last=False):
    if method == "spread":
        if hide_last:
            return ', '.join([str(card) for card in player[:-1]])
        return ', '.join([str(card) for card in player])
    elif method == "sum":
        if hide_last:
            return str(sum([card.value for card in player[:-1]]))
        return str(calculate_scores(player))


def print_scores(player, dealer, hide_dealer=True):
    print(f"\nYour cards: {Fore.CYAN + print_cards(player) + Fore.WHITE} "
          f"[{Fore.MAGENTA + str(calculate_scores(player)) + Fore.WHITE}]")
    if hide_dealer:
        print(f"Dealer cards: {Fore.CYAN + print_cards(dealer, 'spread', hide_dealer) + Fore.WHITE}, (?)"
              f"[{Fore.MAGENTA + print_cards(dealer, 'sum', hide_dealer) + Fore.WHITE}]")
    else:
        print(f"Dealer cards: {Fore.CYAN + print_cards(dealer, 'spread', hide_dealer) + Fore.WHITE} "
              f"[{Fore.MAGENTA + print_cards(dealer, 'sum', hide_dealer) + Fore.WHITE}]")


def draw_cards(n=1):
    cards = []
    for i in range(n):
        card = choice(deck)
        deck.remove(card)
        cards.append(Card(card))
    return cards


def change_aces(player):
    score = calculate_scores(player)
    a_index = [player.index(card) for card in player if card.name == "A" and card.value == 11]
    if score > 21 and a_index:
        for index in a_index:
            player[index].value = 1
            a_index.pop(0)
            score = calculate_scores(player)
            if score <= 21:
                break


def check_scores(player1, player2, check_draw=False):
    player1_score = calculate_scores(player1)
    player2_score = calculate_scores(player2)
    if check_draw:
        if player1_score == player2_score:
            return True
    else:
        if player1_score == 21:
            return True
    return False


def compare_scores(player, dealer):
    player_score = calculate_scores(player)
    dealer_score = calculate_scores(dealer)
    if dealer_score < player_score:
        return True
    if check_scores(player, dealer) and check_scores(dealer, player):
        print(Fore.YELLOW + "\n----------Draw!----------")
        quit()
    elif check_scores(player, dealer, True):
        if calculate_scores(dealer) > 18:
            print(Fore.YELLOW + "\n----------Draw!----------")
            quit()
        else:
            return True
    elif 21 >= player_score > dealer_score:
        print(Fore.GREEN + "\n----------You win!----------")
        quit()
    elif 21 >= dealer_score > player_score:
        print(Fore.RED + "\n----------Dealer wins!----------")
        quit()
    else:
        print(Fore.BLUE + "Unexpected situation:", player_score, dealer_score)
        quit()


def end_game(player, dealer):
    change_aces(player)
    change_aces(dealer)
    print_scores(player, dealer, False)
    while compare_scores(player, dealer):
        dealer.extend(draw_cards())
        change_aces(dealer)
        sleep(1)
        print_scores(player, dealer, False)
        if validate_score(dealer):
            print(Fore.GREEN + "\n----------You win!----------")
            quit()


def game():
    in_game = True
    player = draw_cards(2)
    change_aces(player)
    dealer = draw_cards(2)
    print_scores(player, dealer)

    while in_game:
        button_draw = Fore.GREEN + "'d'" + Fore.WHITE
        button_stand = Fore.GREEN + "'s'" + Fore.WHITE
        print(f"Type {button_draw} to draw a card or {button_stand} to stand: ", end='')
        user_choice = input().lower().strip()
        if user_choice[0] == "d":
            player.extend(draw_cards())
            change_aces(player)
            print_scores(player, dealer)
            if validate_score(player):
                print(Fore.RED + "\n----------Dealer wins!----------")
                quit()
        elif user_choice[0] == "s":
            end_game(player, dealer)
        else:
            print(Fore.YELLOW + "\n----------Invalid choice.----------" + Fore.WHITE)


print("""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
""")
game()
