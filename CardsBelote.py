from random import shuffle

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        
    def __repr__(self):
        return "{} of {}".format(self.value, self.suit)

    def __str__(self):
        return "{}{}".format(self.value[0], self.suit[0].lower())

class Deck:   
    def __init__(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = ["7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
        self.cards = [Card(suit, value) for suit in suits for value in values]

    def get_count(self):
        return len(self.cards)

    def _deal(self, num):
        if num > self.get_count():
            raise ValueError('Not enough cards in the deck')
        cards = self.cards[-num:]
        self.cards = self.cards[:-num]
        return cards

    def shuffle(self):
        shuffle(self.cards)

