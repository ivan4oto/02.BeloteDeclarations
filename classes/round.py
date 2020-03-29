from classes.team import Team
from utils.mixins import Jsonable
from classes.CardsBelote import Deck


class Round(Jsonable):
    NUMBER_OF_TEAMS = 2

    def __init__(self, game_type, ordered_players, number=1):
        self.number = number
        self.game_type = game_type
        self.teams = []
        self.ordered_players = ordered_players

    def __json__(self):
        return {f"round {self.number}": ([team for team in self.teams]), "contract": f"{self.game_type}"}

    def start_round(self):

        deck = self._create_new_deck()
        list_of_decks = self.make_deck_to_four_decks(deck)
        self._add_player_cards(list_of_decks)

    def _create_new_deck(self):
        new_deck = Deck()
        new_deck.shuffle()
        return new_deck

    def _add_player_cards(self, four_deck):

        for player, deck in zip(self.ordered_players, four_deck):
            player.cards = deck

    def make_deck_to_four_decks(self, deck):
        i = 0
        new_list = []
        while i < len(deck.cards):
            new_list.append(deck[i:i + 8])
            i += 8

        return new_list

    def add_round_members(self, teams):
        for team in teams:
            if type(team) != Team:
                raise TypeError
            self.__add_round_member(team)

    def __add_round_member(self, team):
        self.__check_round_members_numbers()

        self.teams.append(team)

    def __check_round_members_numbers(self):

        if len(self.teams) == self.NUMBER_OF_TEAMS:
            raise ValueError

#     she ni trqbva fun za da se razdavat kartite po 8 na player
#     she ni trqbva nesho da opradelq vseki round dali she e No trumps ili All trumps
#     she ni trqbva fun da provqrqva dali nqkoi ot otbtire e stignal do 151
