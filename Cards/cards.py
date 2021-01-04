import random

# Card Games and Objects

# Making Card object


class Card(object):
    # Defining Ranks and Suits. Suits are made with Unicode Characters.
    RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    SUITS = ["♥", "♦", "♣", "♠"]

    def __init__(self, rank, suit):
        self.suit = suit
        self.rank = rank
        self.value = 0

    # Defining rank values. Can change values dependant on game if needed.
        if self.rank == "K":
            self.value = 13
        elif self.rank == "Q":
            self.value = 12
        elif self.rank == "J":
            self.value = 11
        elif self.rank == "10":
            self.value = 10
        elif self.rank == "9":
            self.value = 9
        elif self.rank == "8":
            self.value = 8
        elif self.rank == "7":
            self.value = 7
        elif self.rank == "6":
            self.value = 6
        elif self.rank == "5":
            self.value = 5
        elif self.rank == "4":
            self.value = 4
        elif self.rank == "3":
            self.value = 3
        elif self.rank == "2":
            self.value = 2
        elif self.rank == "A":
            self.value = 14

    # Making Ascii Art of Card for visuals.
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
        """, self.rank, self.suit)
        return rep


# Defining player Hands (or table Hands) object
class Hand(object):
    def __init__(self):
        self.cards = []

    # Used for printing hand. If deck is empty, will print "<EMPTY>"
    def __str__(self):
        if self.cards:
            rep = ""
            for card in self.cards:
                rep += str(card)
        else:
            rep = "<EMPTY>"
        return rep

    # Used for clearing out the hand.
    def clear(self):
        self.cards = []

    # Used for adding a specific card to the hand.
    def add(self, card):
        self.cards.append(card)

    # Used for giving specific cards to other hands.
    def give(self, card, otherHand):
        self.cards.remove(card)
        otherHand.add(card)

    # Used for giving top card to other hands.
    def giveTop(self, otherHand):
        topCard = self.cards[0]
        otherHand.add(topCard)
        self.cards.remove(self.cards[0])


# Defining the Deck.
class Deck(Hand):
    # Shuffles the cards in the deck using random.
    def shuffle(self):
        random.shuffle(self.cards)

    # Populates the deck with all 52 cards.
    def populate(self):
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add(Card(rank, suit))

    # Deals 1 card by default but can change value to whatever number desired to hands.
    def deal(self, hands, perHand=1):
        for rounds in range(perHand):
            for hand in hands:
                if self.cards:
                    topCard = self.cards[0]
                    self.give(topCard, hand)
                else:
                    print("Out of cards, clearing hands and shuffling")
                    self.clear()
                    self.populate()
                    self.shuffle()
                    for hand in hands:
                        hand.clear()
                    self.deal(hands)


# Creating War Card Game
def war():
    # Calling up a new Deck.
    deck = Deck()

    # Defining players and table.
    player1 = Hand()
    player2 = Hand()
    table = Hand()

    # Creating list of hands for deal function, as well as clearing the deck in case it has extra cards, then populating
    # then shuffling and dealing the cards.
    players = [player1, player2]
    deck.clear()
    deck.populate()
    deck.shuffle()
    deck.deal(players, 26)

    # Printing introduction.
    print("Welcome to the Card Game we call War...")
    print("You will draw the first card of your deck of 26 cards.")
    print("The card of the higher value will win, taking the cards on the table.")
    input()
    print("If your cards are of the same value, that is called War.")
    print("You will draw three cards from your deck, same with your opponent.")
    print("If the COMBINED value of your cards is greater than your opponent, you win the war and take all the cards.")
    input()
    print("Whoever is holding all the cards, wins.")
    print("The card values are A = 14, K = 13, Q = 12, J = 11, and the rest of the cards are face value. 10 = 10, 9 = 9, etc.")
    print("If the combined value of your cards in a war are the same, player two takes the cards in this version.")
    print("Otherwise, you would draw an additional 3 cards and the rules of a regular war still apply.")
    input("Press Enter to start playing.")

    # Checks to see if the players have cards.
    while player1.cards and player2.cards:
        # Players put top card down on table.
        player1.giveTop(table)
        player2.giveTop(table)
        # Prints the table.
        print(table)
        input()
        # Checks values of cards. This is if player One's card is higher.
        if table.cards[0].value > table.cards[1].value:
            print("Player One's Card was higher.")
            table.giveTop(player1)
            table.giveTop(player1)
            input()
        # Checks values of cards. This is if player Two's card is higher.
        elif table.cards[0].value < table.cards[1].value:
            print("Player Two's Card was higher.")
            table.giveTop(player2)
            table.giveTop(player2)
            input()
        # Checks values of cards. This is if both players have the same value.
        else:
            # Checks to see if players have enough cards to play a war.
            if len(player1.cards) >= 3 and len(player2.cards) >= 3:
                print("WAR!")
                # Player 1 and 2 both place 3 cards on the table.
                player1.giveTop(table)
                player1.giveTop(table)
                player1.giveTop(table)
                player2.giveTop(table)
                player2.giveTop(table)
                player2.giveTop(table)
                print(table)
                input()
                # Combines and checks values of cards. This is if player 1's value is higher.
                if table.cards[2].value + table.cards[3].value + table.cards[4].value > table.cards[5].value + table.cards[6].value + table.cards[7].value:
                    print("Player One Wins The War")
                    for card in table.cards:
                        table.giveTop(player1)
                    input()
                # Combines and checks values of cards. This is if player 2's value is higher,
                # or their values are the same.
                else:
                    print("Player Two Wins The War")
                    for card in table.cards:
                        table.giveTop(player2)
                    input()
            # This is if the players do not have enough cards to play a war.
            else:
                # Checks who has more cards, and gives the opponents cards to them. This is if player 1 has more cards.
                if len(player1.cards) > len(player2.cards):
                    for card in player2.cards:
                        player2.giveTop(player1)
                # Checks who has more cards, and gives the opponents cards to them. This is if player 2 has more cards.
                else:
                    for card in player1.cards:
                        player1.giveTop(player2)
                break
    # Checking who has all the cards. This is if player 1 has them all.
    if player1.cards:
        print("Player 1 wins.")
    # Checking who has all the cards. This is if player 2 has them all.
    else:
        print("Player 2 wins.")


# Declaring war function in main program.
war()
