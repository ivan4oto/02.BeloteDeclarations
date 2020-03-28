from random import random
from copy import copy, deepcopy

from classes.round import Round
from utils.mixins import Jsonable


class Game(Jsonable):
    MAX_SCORE = 151

    def __init__(self, teams, game_number=1):
        self.rounds = []
        self.game_number = game_number
        self.teams = teams
        self.current_round = 1
        self.winner = False

    def __json__(self):
        return {f"game {self.game_number}": ([round_game for round_game in self.rounds])}

    def start_game(self):

        while not type(self.winner):
            self.star_rounds()

    def star_rounds(self):

        while not self.check_for_game_winner():
            self.__clear_for_new_round()
            new_round = Round(self.take_round_type(), self.current_round)
            new_round.add_round_members(self.teams)
            self.rounds.append(new_round)

            self.current_round += 1

    def __clear_for_new_round(self):
        for team in self.teams:
            team.new_round()

    def take_round_type(self):

        all_types = ["All trumps", "No trumps"]
        return random(all_types)

    def check_for_game_winner(self):

        first_team_total = self.teams[0].collect_total_points()
        second_team_total = self.teams[1].collect_total_points()

        if first_team_total == second_team_total:
            return False
        elif self.__check_for_max_score(first_team_total):
            self.winner = self.teams[0]
            return True
        elif self.__check_for_max_score(second_team_total):
            self.winner = self.teams[1]
            return True

    def __check_for_max_score(self, team_total):
        if team_total >= self.MAX_SCORE:
            return True
        else:
            return False


class Games(Jsonable):
    TWO_GAMES_WINNER = 2

    def __init__(self, teams):
        self.games = {}  # key e otbor  a value e list ot specelinite igri
        self.closed_games = []
        self.games_played = 1
        self.teams = teams
        self.games_winners = False

    def __json__(self):
        return {f"Belote Game": ([game for game in self.closed_games])}

    def start_games(self):

        while not self.check_for_two_games_winner():

            game = Game(self.teams, self.games_played)

            game.start_game()

            if game.winner in self.games:
                self.teams[game.winner] = 1
            else:
                self.teams[game.winner] += 1

            self.games_played += 1
            self.closed_games.append(deepcopy(game))

    def clear_for_new_game(self):
        for team in self.teams:
            team.new_game()

    def check_for_two_games_winner(self):
        for key, value in self.games.items():
            if len(value) == self.TWO_GAMES_WINNER:
                self.games_winners = key
                return True
        return False
