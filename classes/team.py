from classes.player import Player


class Team:
    NUMBER_OF_MEMBERS = 2

    def __init__(self, name):
        self.name = name
        self.players = []

    def new_round(self):
        for member in self.players:
            member.new_round()

    def add_team_members(self, members):
        for member in members:
            if type(member) != Player:
                raise TypeError
            self.__add_team_member(member)

    def __add_team_member(self, member):
        self.__check_team_members_numbers()

        self.players.append(member)

    def __check_team_members_numbers(self):

        if len(self.players) == self.NUMBER_OF_MEMBERS:
            raise ValueError

    def collect_total_points(self):
        all_points = 0
        for member in self.players:
            point = member.all_points()
            all_points += point

        return all_points
