import json
import unittest

from utils.mixins import Jsonable, OurEncoder
from classes.player import Player
from classes.round import Round
from classes.team import Team
from classes.game import Game


class TestJsonable(unittest.TestCase):
    def test_player_jsonable(self):
        player = Player("Marto")

        self.assertEqual(player.to_json(),
                         json.dumps({"Marto": {"points": 0, "announcements": [], "cards": []}},
                                    cls=OurEncoder))

    def test_team_jsonable(self):
        player1 = Player("Marto")
        player2 = Player("Pesho")

        team1 = Team("Wolf")
        team1.add_team_members([player1, player2])

        self.assertEqual(team1.to_json(), json.dumps({"Wolf": [
            {"Marto": {"points": 0, "announcements": [], "cards": []}},
            {"Pesho": {"points": 0, "announcements": [], "cards": []}}]},
            cls=OurEncoder))

    def test_round_jsonable(self):
        player1 = Player("Marto")
        player2 = Player("Pesho")
        player3 = Player("Nasko")
        player4 = Player("Petko")

        team1 = Team("Wolf")
        team2 = Team("Lion")
        team1.add_team_members([player1, player2])
        team2.add_team_members([player3, player4])

        round1 = Round("All trumps", 1)
        round1.add_round_members([team1, team2])

        self.assertEqual(round1.to_json(), json.dumps({"round 1": [
            {"Wolf": [
                {"Marto": {"points": 0, "announcements": [], "cards": []}},
                {"Pesho": {"points": 0, "announcements": [], "cards": []}}]},
            {"Lion": [
                {"Nasko": {"points": 0, "announcements": [], "cards": []}},
                {"Petko": {"points": 0, "announcements": [], "cards": []}}]}
        ],
            "contract": "All trumps"}, cls=OurEncoder))

    def test_game_jsonable(self):
        player1 = Player("Marto")
        player2 = Player("Pesho")
        player3 = Player("Nasko")
        player4 = Player("Petko")

        team1 = Team("Wolf")
        team2 = Team("Lion")
        team1.add_team_members([player1, player2])
        team2.add_team_members([player3, player4])

        round1 = Round("All trumps", 1)
        round1.add_round_members([team1, team2])

        game = Game([team1, team2], 1)
        game.rounds.append(round1)

        self.assertEqual(game.to_json(), json.dumps({"game 1": [
            {"round 1": [
                {"Wolf": [
                    {"Marto": {"points": 0, "announcements": [], "cards": []}},
                    {"Pesho": {"points": 0, "announcements": [], "cards": []}}]},
                {"Lion": [
                    {"Nasko": {"points": 0, "announcements": [], "cards": []}},
                    {"Petko": {"points": 0, "announcements": [], "cards": []}}]}
            ],
                "contract": "All trumps"}]}, cls=OurEncoder))


if __name__ == '__main__':
    unittest.main()
