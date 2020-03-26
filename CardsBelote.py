from random import shuffle

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    def __repr__(self):
        return "{} of {}".format(self.value, self.suit)

class Deck:   
    def __init__(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = ["7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
        self.cards = [Card(suit, value) for suit in suits for value in values]

    def get_count(self):
        return len(self.cards)

    def _deal(self, num):
        pass

    def shuffle(self):
        shuffle(self.cards)

