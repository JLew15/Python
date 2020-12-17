import random

class Card(object):
    RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    SUITS =["♥", "♦", "♣", "♠"]

    def __init__(self, rank, suit):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        rep = str.format("""
        +--------+
        | {1}{0:2}    |
        |        |
        |        |
        |        |
        |        |
        |        |
        |    {0:2}{1} |
        +--------+
        """,self.rank,self.suit)
        return rep



hand = []
for i in range(5):
    suit = random.choice(Card.SUITS)
    rank = random.choice(Card.RANKS)
    card = Card(rank,suit)
    hand.append(card)
for card in hand:
    print(card)
