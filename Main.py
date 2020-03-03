from Deck import Deck

import sys

dealername = "Dan"
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
    for i in range(0, 7):
        decks[i].shuffle()
        print(str(decks[i]))


print(f"Hey, I'm your dealer, {dealername}. Before we begin, wanna see the cards in the shoe? I'm not cheating ya. (yes or no).")





if input(answer) == "yes":
    for i in range(0, 7):
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
    sys.exit()



