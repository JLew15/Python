import cards
import gameFunctions as gF


class BlackJackCards(cards.PosCard):
    ACE_VALUE = 1

    @property
    def value(self):
        if self.faceUp:
            value = BlackJackCards.RANKS.index(self.rank) + 1
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

    def __str__(self):
        print("###################################")
        for card in self.cards:
            print(card)
        rep = "###################################"
        rep += "\n " + self.name
        rep += "\n " + self.total
        return rep

    @property
    def total(self):
        for card in self.cards:
            if not card.value:
                return None
        t = 0
        for card in self.cards:
            t += card.value

        hasAce = False
        for card in self.cards:
            if card.value == BlackJackCards.ACE_VALUE:
                hasAce = True

        if hasAce and t <= 11:
            t += 10
        return t

    def isBusted(self):
        return self.total > 21


class BlackJackPlayer(BlackJackHand):
    def bust(self):
        print(self.name, "busts.")
        self.lose()

    def lose(self):
        print(self.name, "loses.")

    def win(self):
        print(self.name, "wins")

    def push(self):
        print(self.name, "pushes")

    def isHitting(self):
        response = gF.yesNo("\n" + self.name + ", do you want a hit? Yes or No: ")
        return response == "y"


class BlackJackDealer(BlackJackHand):
    def isHitting(self):
        return self.total < 17

    def bust(self):
        print(self.name, "busts.")

    def flipFirstCard(self):
        self.cards[0].flip()


class Game(object):
    def __init__(self, names):
        self.deck = BlackJackDeck
        self.deck.populate()
        self.deck.shuffle()
        self.dealer = BlackJackDealer("Dealer")
        self.players = []
        for name in names:
            player = BlackJackPlayer(name)
            self.players.append(player)

    @property
    def stillPlaying(self):
        sp = []
        for player in self.players:
            if not player.isBusted():
                sp.append(player)
        return sp


deck = BlackJackDeck()
deck.populate()
deck.shuffle()

testCard = deck.cards[0]
print(testCard)
print(testCard.value)
