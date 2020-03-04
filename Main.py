from Deck import Deck

import sys
import random

dealers =  [
    "Danny Devito",
    "Long S. Chlong",
    "Dr. Prepper",
    "Phil Swift",
    "Oliver Closeoff",
    "Papa B. Owner",
    "Mr. PoopyButtHole",
    "Broc Lee",
    "Mike Bloomberg, brought to you by Mike Bloomberg",
    "Vermin Supreme",
    "GENERATING WITTY NAME, PLEASE WAIT.."
]

answer: str = ""
answer2: str = ""

decks = [
    Deck(),
    Deck(),
    Deck(),
    Deck(),
    Deck(),
    Deck(),
    Deck(),
    Deck(),
    Deck()
]

def shoe(decks):
    for i in range(0, 8):
        decks[i].shuffle()
        print(str(decks[i]))

def deal():
    ran = random.randint(0, len(dealers) - 1)
    dealername = dealers[ran]
    print(
        f"Hey, I'm your dealer, {dealername}. Before we begin, wanna see the cards in the shoe? I'm not cheating ya, eight decks. (yes or no).")

    if input(answer) == "yes":
        for i in range(0, 8):
            print(str(decks[i]))

    else:
        shoe(decks)
        print("Okay, here's your cards.")
        sys.exit()

    print("Alright, can I shuffle now?")

    if input(answer2) == "yes":
        shoe(decks)
        print("There you go. I don't know what you want with this deck, but whatever.")
    else:
        print("Man, this ain't twenty questions. Find a new dealer.")
        deal()

deal()






