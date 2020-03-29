import itertools


class Player:
    def __init__(self, name):
        self.name = name
        self.all_points = 0
        self.cards = []
        self.announcements = []
        self.round_report = {}  # pazi kakav announcements v segashniqt round imame i kartite

    def __repr__(self):
        return f"{self.name} - {self.all_points} - {self.cards} "

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

    def hand_size(self):
        return len(self.cards)

    def add_round_report(self):
        self.announcements.extend(self.round_report)

    def check_for_announcements(self):
        #group same value
        x = [list(j) for i, j in itertools.groupby(self.cards)]
        annsCarre = []
        annsConsec  = []

        #find Carre
        for i in x:
            if len(i) == 4:
                if i[0].get_key() in (4,6,7,9):
                    annsCarre.append("carre of {}'s = 100 points".format(i[0].value))
                elif i[0].get_key() == 3:
                    annsCarre.append("carre of {}'s = 150 points".format(i[0].value))
                elif i[0].get_key() == 5:
                    annsCarre.append("carre of {}'s = 200 points".format(i[0].value))
        
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
        #finds Tierce, Quarte or Quinte
        for grp in groups:
            if len(grp) == 3:
                annsConsec.append('tierce')
            elif len(grp) == 4:
                annsConsec.append('quarte')
            elif len(grp) >= 5:
                annsConsec.append('quinte')


        self.announcements.append(annsCarre)
        self.announcements.append(annsConsec)
        
def main():
    pass

if __name__ == "__main__":
    main()