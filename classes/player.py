from mixins import Jsonable
from CardsBelote import Card, Deck
import itertools


class Player(Jsonable):
    def __init__(self, name):
        self.name = name
        self.all_points = 0
        self.cards = []
        self.announcements = []
        self.round_report = {}  # pazi kakav announcements v segashniqt round imame i kartite

    def __repr__(self):
        return f"{self.name} - {self.all_points} - {self.cards} "

    def __json__(self):
        return {f"{self.name}": {
            "points": self.all_points, "announcements": self.announcements, "cards": self.cards}}

    def add_cards(self, cards):
        for card in cards:
            self.__add_card(card)

    def __add_card(self, card):
        if len(self.cards) == 8:
            raise ValueError

        self.cards.append(card)

    def new_round(self):
        self.cards = []
        self.round_report = {}

    def new_game(self):
        self.announcements = []
        self.all_points = 0
        self.cards = []
        self.round_report = {}

    def hand_size(self):
        return len(self.cards)

    def add_round_report(self):
        self.announcements.extend(self.round_report)

    def check_for_announcements(self,gametype):
        anns = {}

        #find Belote 
        def find_belote_anns(gametype):
            if gametype == "All trumps":
                for a in self.cards:
                    if a.value == 'Queen':
                        b = Card(a.suit, 'King')
                        if b in self.cards:
                            anns['belote'] = [a,b]
            elif gametype in ['Hearts', 'Diamonds', 'Clubs', 'Spades']:
                for a in self.cards:
                    if a == Card(gametype, 'Queen'):
                        b = Card(a.suit, 'King')
                        if b in self.cards:
                            anns['belote'] = [a,b]

        #find Carre
        def find_carre_anns(gametype):
            if gametype != 'No trumps':
                #group same value
                x = [list(j) for i, j in itertools.groupby(self.cards)]
                for i in x:
                    if len(i) == 4:
                        if i[0].get_key() in (4,6,7,9):
                            anns["carre of {}'s = 100 points".format(i[0].value)] = i
                        elif i[0].get_key() == 3:
                            anns["carre of {}'s = 150 points".format(i[0].value)] = i
                        elif i[0].get_key() == 5:
                            anns["carre of {}'s = 200 points".format(i[0].value)] = i
        
        #finds Tierce, Quarte or Quinte
        def find_consecutive_anns(gametype):
            if gametype != 'No trumps':
                #Groups cards into consecutive values
                def groupSequence(lst):
                    res = [[lst[0]]]
                    for i in range(1, len(lst)):
                        #get_key used to compare the coresponding value in valuesDict
                        if (lst[i-1]).get_key()+1 == (lst[i]).get_key():
                            res[-1].append(lst[i])
                        else:
                            res.append([lst[i]])
                    return res

                groups = groupSequence(self.cards)
                for grp in groups:
                    if len(grp) == 3:
                        anns['tierce'] = grp
                    elif len(grp) == 4:
                        anns['quarte'] = grp
                    elif len(grp) >= 5:
                        anns['quinte'] = grp

        find_carre_anns(gametype)
        find_consecutive_anns(gametype)
        find_belote_anns(gametype)
        self.round_report  = anns




def main():
    pass
    
if __name__ == "__main__":
    main()