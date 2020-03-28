from classes.team import Team
from utils.mixins import Jsonable


class Round(Jsonable):
    NUMBER_OF_TEAMS = 2

    def __init__(self, game_type, number=1):
        self.number = number
        self.game_type = game_type
        self.teams = []

    def __json__(self):
        return {f"round {self.number}": ([team for team in self.teams])}

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
