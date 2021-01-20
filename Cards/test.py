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
        if self.total:
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
        self.deck = BlackJackDeck()
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

    def __additionalCards(self, player):
        while not player.isBusted() and player.isHitting():
            self.deck.deal([player], 1)
            print(player)
            if player.isBusted():
                player.bust()

    def play(self):
        self.deck.deal(self.players + [self.dealer], 2)
        self.dealer.flipFirstCard()
        print(self.dealer)

        for player in self.players:
            self.__additionalCards(player)

        self.dealer.flipFirstCard()
        if not self.stillPlaying:
            print(self.dealer)
        else:
            print(self.dealer)
            self.__additionalCards(self.dealer)
            if self.dealer.isBusted():
                for player in self.stillPlaying:
                    player.win()
            else:
                for player in self.stillPlaying:
                    if player.total > self.dealer.total:
                        player.win()
                    elif player.total == self.dealer.total:
                        player.push()
                    else:
                        player.lose()
        for player in self.players:
            player.clear()
        self.dealer.clear()


def main():
    print("\t\tWelcome to Black Jack!\n")

    names = []
    numPlayers = gF.getNumber("How many players are playing?", 8, 1)
    for i in range(numPlayers):
        name = gF.getName()
        names.append(name)
    game = Game(names)
    play = None
    while play != "n":
        game.play()
        play = gF.yesNo("\nDo you want to play again?: ")


main()
