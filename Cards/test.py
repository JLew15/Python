import cards
import gameFunctions as gf

class BlackJackCards(cards.PosCard):
    ACE_VALUE = 1

    @property
    def value(self):
        if self.faceUp:
            value = BlackJackCards.RANKS.index(self.rank)+1
            if value > 10:
                value = 10
        else:
            value = None
        return value

class BlackJackDeck(cards.Deck):
    def populate(self):
        for suit in cards.Card.SUITS:
            for rank in cards.Card.RANKS:
                self.add(BlackJackCards(rank, suit))

class BlackJackHand(cards.Hand):
    def __init__(self, name):
        super(BlackJackHand, self).__init__()
        self.name = name


deck = BlackJackDeck()
deck.populate()
deck.shuffle()


testCard = deck.cards[0]
print(testCard)
print(testCard.value)