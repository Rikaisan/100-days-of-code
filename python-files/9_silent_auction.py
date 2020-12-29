from os import system

bids = dict()


def check_for_people():
    more_people = input("Are there more people? (yes/no)\n").lower().strip()
    while True:
        if more_people[0] == 'y':
            return True
        elif more_people[0] == 'n':
            return False
        more_people = input("Invalid answer, are there more people? (yes/no)\n").lower().strip()


while True:
    name = input("Please type your name: ").strip().title()
    bid = input("Type your bid (Only full numbers): $")
    while type(bid) != int:
        # noinspection PyBroadException
        try:
            bid = int(bid)
        except Exception:
            bid = input("Please enter a valid bid (Only full numbers): $")
    bids.update({bid: name})
    if not check_for_people():
        system("clear")
        break
    else:
        system("clear")
        continue


max_bid = max(bids.keys())
max_bidder = bids.get(max_bid)

print(f"The winner is {max_bidder} with a bid of ${max_bid:,} USD!")
