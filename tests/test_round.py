import unittest

from classes.CardsBelote import Deck
from classes.player import Player
from classes.round import Round
from classes.team import Team


class TestRound(unittest.TestCase):
    def test_add_round_members_when_give_correct_inputs_return_correct(self):
        player1 = Player("Marto")
        player2 = Player("Pesho")
        player3 = Player("Nasko")
        player4 = Player("Petko")

        team1 = Team("Wolf")
        team2 = Team("Lion")
        team1.add_team_members([player1, player2])
        team2.add_team_members([player3, player4])

        ordered_players = [player1, player3, player2, player4]

        new_round = Round("All trumps", ordered_players, 1)
        new_round.add_round_members([team1, team2])

        self.assertEqual(new_round.teams, [team1, team2])

    def test_add_round_members_when_give_string_inputs_return_exception(self):
        player3 = Player("Nasko")
        player4 = Player("Petko")

        team2 = Team("Lion")
        team2.add_team_members([player3, player4])

        ordered_players = [player3, player4]

        new_round = Round("All trumps", ordered_players, 1)

        with self.assertRaises(TypeError):
            new_round.add_round_members(["There is no team", team2])

    def test_add_round_members_when_give_player_obj_inputs_return_exception(self):
        player3 = Player("Nasko")
        player4 = Player("Petko")

        team2 = Team("Lion")
        team2.add_team_members([player3, player4])

        ordered_players = [player3, player4]

        new_round = Round("All trumps", ordered_players, 1)

        with self.assertRaises(TypeError):
            new_round.add_round_members([player4, team2])

    def test_make_deck_to_four_decks_when_give_a_deck_return_list_of_decks(self):
        new_deck = Deck()

        player1 = Player("Marto")
        player2 = Player("Pesho")
        player3 = Player("Nasko")
        player4 = Player("Petko")

        team1 = Team("Wolf")
        team2 = Team("Lion")
        team1.add_team_members([player1, player2])
        team2.add_team_members([player3, player4])

        ordered_players = [player1, player3, player2, player4]

        new_round = Round("All trumps", ordered_players, 1)
        new_round.add_round_members([team1, team2])

        list_of_deck = new_round.make_deck_to_four_decks(new_deck)

        self.assertEqual(len(list_of_deck), 4)


if __name__ == '__main__':
    unittest.main()
