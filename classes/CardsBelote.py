from random import shuffle


class Card:
    valuesDict = {
        '7': 1,
        '8': 2,
        '9': 3,
        '10': 4,
        'Jack': 5,
        'Queen': 6,
        'King': 7,
        'Ace': 9
        }

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        
    def __repr__(self):
        return "{} of {}".format(self.value, self.suit)

    def __str__(self):
        #Cards with value '10' were returning '1' as a value before the if statement.
        if self.value == '10':
            return "{}{}".format(self.value[:2], self.suit[0].lower())
        else:
            return "{}{}".format(self.value[0], self.suit[0].lower())


    def __eq__(self, other):
        return self.valuesDict[self.value] == self.valuesDict[other.value]

    def __lt__(self, other):
        return self.valuesDict[self.value] < self.valuesDict[other.value]

    def __gt__(self, other):
        return self.valuesDict[self.value] > self.valuesDict[other.value]

    def __le__(self, other):
        return self.valuesDict[self.value] <= self.valuesDict[other.value]




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

    def __getitem__(self, cardnum):
        return self.cards[cardnum]   

    def __str__(self):
        return str([str(card) for card in self.cards])

    def shuffle(self):
        shuffle(self.cards)