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
        self.start_player_announcements()

    def start_player_announcements(self):

        for team in self.teams:
            team.players[0].check_for_announcements(self.game_type)
            team.players[1].check_for_announcements(self.game_type)

    def check_teams_for_quinte(self):
        first_team_report = self.teams[0].take_players_round_report()
        second_team_report = self.teams[1].take_players_round_report()

        if self.check_team_for_quinte(first_team_report) and self.check_team_for_quinte(second_team_report):
            dict_to_check = {}
            for player, report in first_team_report.items():
                if "quinte" in report:
                    dict_to_check[sum([card.valuesDict(card.value) for card in report["quinte"]])] = [player]

            for player, report in second_team_report.items():
                if "quinte" in report:
                    dict_to_check[sum([card.valuesDict(card.value) for card in report["quinte"]])] = [player]

            max_value = max(dict_to_check.keys())
            winner = [dict_to_check[max_value]]

            if len(winner) == 2:
                for player, values in second_team_report.items():
                    if "quinte" in values:
                        del values['quinte']
                        self.remove_tierce_and_quarte(second_team_report)
                for player, values in first_team_report.items():
                    if "quinte" in values:
                        del values['quinte']
                        self.remove_tierce_and_quarte(first_team_report)

            else:
                if not winner in first_team_report:
                    for player, values in second_team_report.items():
                        if "quinte" in values:
                            del values['quinte']
                        self.remove_tierce_and_quarte(second_team_report)
                else:
                    for player, values in first_team_report.items():
                        if "quinte" in values:
                            del values['quinte']
                        self.remove_tierce_and_quarte(first_team_report)

        elif self.check_team_for_quinte(first_team_report):

            self.remove_tierce_and_quarte(second_team_report)

        elif self.check_team_for_quinte(second_team_report):

            self.remove_tierce_and_quarte(first_team_report)

    def remove_tierce_and_quarte(self, team_report):
        for player, report in team_report.items():
            if "tierce" in report:
                del report['tierce']
            if "quarte" in report:
                del report['quarte']

    def check_team_for_quinte(self, team_report):
        for player, report in team_report.items():
            if "quinte" in report:
                return True

    def check_teams_for_quarte(self):

        first_team_report = self.teams[0].take_players_round_report()
        second_team_report = self.teams[1].take_players_round_report()

        if self.check_team_for_quarte(first_team_report) and self.check_team_for_quarte(second_team_report):

            dict_to_check = {}
            for player, report in first_team_report.items():
                if "quarte" in report:
                    dict_to_check[sum([card.valuesDict(card.value) for card in report["quarte"]])] = [player]

            for player, report in second_team_report.items():
                if "quarte" in report:
                    dict_to_check[sum([card.valuesDict(card.value) for card in report["quarte"]])] = [player]

            max_value = max(dict_to_check.keys())
            winner = [dict_to_check[max_value]]

            if len(winner) == 2:
                for player, values in second_team_report.items():
                    if "quarte" in values:
                        del values['quarte']
                        self.remove_tierce(second_team_report)
                for player, values in first_team_report.items():
                    if "quarte" in values:
                        del values['quarte']
                        self.remove_tierce(first_team_report)

            else:
                if not winner in first_team_report:
                    for player, values in second_team_report.items():
                        if "quarte" in values:
                            del values['quarte']
                        self.remove_tierce(second_team_report)
                else:
                    for player, values in first_team_report.items():
                        if "quarte" in values:
                            del values['quarte']
                        self.remove_tierce(first_team_report)
        elif self.check_team_for_quarte(first_team_report):
            self.remove_tierce(second_team_report)

        elif self.check_team_for_quarte(second_team_report):
            self.remove_tierce(first_team_report)

    def check_team_for_quarte(self, team_report):
        for player, report in team_report.items():
            if "quarte" in report:
                return True

    def remove_tierce(self, team_report):
        for player, report in team_report.items():
            if "tierce" in report:
                del report['tierce']

    def check_teams_for_tierce(self):

        first_team_report = self.teams[0].take_players_round_report()
        second_team_report = self.teams[1].take_players_round_report()

        if self.check_team_for_tierce(first_team_report) and self.check_team_for_tierce(second_team_report):

            dict_to_check = {}
            for player, report in first_team_report.items():
                if "tierce" in report:
                    dict_to_check[sum([card.valuesDict(card.value) for card in report["tierce"]])] = [player]

            for player, report in second_team_report.items():
                if "tierce" in report:
                    dict_to_check[sum([card.valuesDict(card.value) for card in report["tierce"]])] = [player]

            max_value = max(dict_to_check.keys())
            winner = [dict_to_check[max_value]]

            if len(winner) == 2:
                for player, values in second_team_report.items():
                    if "tierce" in values:
                        del values['tierce']
                for player, values in first_team_report.items():
                    if "tierce" in values:
                        del values['tierce']
            else:
                if not winner in first_team_report:
                    for player, values in second_team_report.items():
                        if "tierce" in values:
                            del values['tierce']
                else:
                    for player, values in first_team_report.items():
                        if "tierce" in values:
                            del values['tierce']

    def check_team_for_tierce(self, team_report):
        for player, report in team_report.items():
            if "tierce" in report:
                return True

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
