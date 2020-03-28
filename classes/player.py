from utils.mixins import Jsonable


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

    def check_for_announcements(self):
        # proverqva broq na kartite dali e 8 i ako e 8 proverqva dali imash combinaciq
        if len(self.cards) != 8:
            raise ValueError
