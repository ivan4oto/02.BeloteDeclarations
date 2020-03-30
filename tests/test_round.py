import unittest

from classes.CardsBelote import Deck, Card
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

    def test_add_player_cards_when_add_correct_deck_to_player_return_correct(self):
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

        new_round._add_player_cards(list_of_deck)

        self.assertEqual(len(player1.cards), 8)
        self.assertEqual(len(player2.cards), 8)
        self.assertEqual(len(player3.cards), 8)
        self.assertEqual(len(player4.cards), 8)

    def test_check_teams_for_quinte_when_add_to_two_teams_quinte_return_correct(self):
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

        new_round = Round("Diamonds", ordered_players, 1)
        new_round.add_round_members([team1, team2])

        list_of_deck = new_round.make_deck_to_four_decks(new_deck)

        new_round._add_player_cards(list_of_deck)

        player1.cards = [Card('Diamonds', '7'),
                         Card('Diamonds', '8'),
                         Card('Diamonds', '9'),
                         Card('Diamonds', '10'),
                         Card('Diamonds', 'Jack'),
                         Card('Diamonds', 'Queen'),
                         Card('Diamonds', 'King'),
                         Card('Diamonds', 'Ace')]

        player2.cards = [Card('Clubs', 'Ace'),
                         Card('Clubs', '10'),
                         Card('Clubs', '8'),
                         Card('Clubs', 'Jack'),
                         Card('Clubs', '7'),
                         Card('Clubs', 'Queen'),
                         Card('Clubs', 'King'),
                         Card('Clubs', '9')]

        player3.cards = [Card('Spades', 'Ace'),
                         Card('Spades', '10'),
                         Card('Spades', '8'),
                         Card('Spades', 'Jack'),
                         Card('Spades', '7'),
                         Card('Spades', 'Queen'),
                         Card('Spades', 'King'),
                         Card('Spades', '9')]

        player4.cards = [Card('Hearts', 'Ace'),
                         Card('Hearts', '10'),
                         Card('Hearts', '8'),
                         Card('Hearts', 'Jack'),
                         Card('Hearts', '7'),
                         Card('Hearts', 'Queen'),
                         Card('Hearts', 'King'),
                         Card('Hearts', '9')]
        new_round.start_player_announcements()

        new_round.check_teams_for_quinte()

        self.assertEqual(len(player1.round_report), 2)
        self.assertEqual(len(player2.round_report), 1)
        self.assertEqual(len(player3.round_report), 1)
        self.assertEqual(len(player4.round_report), 1)

    def test_check_teams_for_quinte_when_add_to_player_quinte_other_team_tierce_return_remove_tierce(self):
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

        new_round = Round("Diamonds", ordered_players, 1)
        new_round.add_round_members([team1, team2])

        list_of_deck = new_round.make_deck_to_four_decks(new_deck)

        new_round._add_player_cards(list_of_deck)

        player1.cards = [Card('Diamonds', '7'),
                         Card('Diamonds', '8'),
                         Card('Diamonds', '9'),
                         Card('Diamonds', '10'),
                         Card('Diamonds', 'Jack'),
                         Card('Diamonds', 'Queen'),
                         Card('Diamonds', 'King'),
                         Card('Diamonds', 'Ace')]

        player2.cards = [Card('Clubs', 'Ace'),
                         Card('Clubs', '10'),
                         Card('Clubs', '8'),
                         Card('Clubs', 'Jack'),
                         Card('Clubs', '7'),
                         Card('Clubs', 'Queen'),
                         Card('Clubs', 'King'),
                         Card('Clubs', '9')]

        player3.cards = [Card('Spades', '7'),
                         Card('Spades', '8'),
                         Card('Spades', '9'),
                         Card('Spades', 'Ace'),
                         Card('Spades', '10'),
                         Card('Spades', 'Jack'),
                         Card('Spades', 'Queen'),
                         Card('Spades', 'King')
                         ]

        player4.cards = [Card('Hearts', 'Ace'),
                         Card('Hearts', '10'),
                         Card('Hearts', '8'),
                         Card('Hearts', 'Jack'),
                         Card('Hearts', '7'),
                         Card('Hearts', 'Queen'),
                         Card('Hearts', 'King'),
                         Card('Hearts', '9')]
        new_round.start_player_announcements()
        new_round.check_teams_for_quinte()

        self.assertEqual(len(player1.round_report), 2)
        self.assertEqual(len(player2.round_report), 1)
        self.assertEqual(len(player3.round_report), 1)
        self.assertEqual(len(player4.round_report), 1)

    def test_check_teams_for_quarte_when_add_to_player_quarte_and_other_team_have_tierce(self):
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

        new_round = Round("Diamonds", ordered_players, 1)
        new_round.add_round_members([team1, team2])

        list_of_deck = new_round.make_deck_to_four_decks(new_deck)

        new_round._add_player_cards(list_of_deck)

        player1.cards = [Card('Diamonds', '7'),
                         Card('Diamonds', '8'),
                         Card('Diamonds', '9'),
                         Card('Diamonds', '10'),
                         Card('Diamonds', 'Queen'),
                         Card('Diamonds', 'Jack'),
                         Card('Diamonds', 'Ace'),
                         Card('Diamonds', 'King')]

        player2.cards = [Card('Clubs', 'Ace'),
                         Card('Clubs', '10'),
                         Card('Clubs', '8'),
                         Card('Clubs', 'Jack'),
                         Card('Clubs', '7'),
                         Card('Clubs', 'Queen'),
                         Card('Clubs', 'King'),
                         Card('Clubs', '9')]

        player3.cards = [Card('Spades', 'King'),
                         Card('Spades', '8'),
                         Card('Spades', 'Ace'),
                         Card('Spades', '10'),
                         Card('Spades', 'Jack'),
                         Card('Spades', 'Queen'),
                         Card('Spades', '7'),
                         Card('Spades', '9'),
                         ]

        player4.cards = [Card('Hearts', 'Ace'),
                         Card('Hearts', '10'),
                         Card('Hearts', '8'),
                         Card('Hearts', 'Jack'),
                         Card('Hearts', '7'),
                         Card('Hearts', 'Queen'),
                         Card('Hearts', 'King'),
                         Card('Hearts', '9')]
        new_round.start_player_announcements()
        new_round.check_teams_for_quarte()

        self.assertEqual(len(player1.round_report), 2)
        self.assertEqual(len(player2.round_report), 1)
        self.assertEqual(len(player3.round_report), 1)
        self.assertEqual(len(player4.round_report), 1)

    def test_check_teams_for_quarte_when_two_teams_have_quarte_remove_quarte_both(self):
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

        new_round = Round("Diamonds", ordered_players, 1)
        new_round.add_round_members([team1, team2])

        list_of_deck = new_round.make_deck_to_four_decks(new_deck)

        new_round._add_player_cards(list_of_deck)

        player1.cards = [Card('Diamonds', '7'),
                         Card('Diamonds', '8'),
                         Card('Diamonds', '9'),
                         Card('Diamonds', '10'),
                         Card('Diamonds', 'Queen'),
                         Card('Diamonds', 'Jack'),
                         Card('Diamonds', 'Ace'),
                         Card('Diamonds', 'King')]

        player2.cards = [Card('Clubs', 'Ace'),
                         Card('Clubs', '10'),
                         Card('Clubs', '8'),
                         Card('Clubs', 'Jack'),
                         Card('Clubs', '7'),
                         Card('Clubs', 'Queen'),
                         Card('Clubs', 'King'),
                         Card('Clubs', '9')]

        player3.cards = [Card('Spades', 'King'),
                         Card('Spades', '8'),
                         Card('Spades', 'Ace'),
                         Card('Spades', '10'),
                         Card('Spades', 'Jack'),
                         Card('Spades', 'Queen'),
                         Card('Spades', '7'),
                         Card('Spades', '9'),
                         ]

        player4.cards = [Card('Hearts', '7'),
                         Card('Hearts', '8'),
                         Card('Hearts', '9'),
                         Card('Hearts', '10'),
                         Card('Hearts', 'Queen'),
                         Card('Hearts', 'Jack'),
                         Card('Hearts', 'Ace'),
                         Card('Hearts', 'King')
                         ]
        new_round.start_player_announcements()
        new_round.check_teams_for_quarte()

        self.assertEqual(len(player1.round_report), 1)
        self.assertEqual(len(player2.round_report), 1)
        self.assertEqual(len(player3.round_report), 1)
        self.assertEqual(len(player4.round_report), 1)

    def test_check_teams_for_quarte_when_two_teams_have_quarte_remove_weaker_quarte(self):
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

        new_round = Round("Hearts", ordered_players, 1)
        new_round.add_round_members([team1, team2])

        list_of_deck = new_round.make_deck_to_four_decks(new_deck)

        new_round._add_player_cards(list_of_deck)

        player1.cards = [Card('Diamonds', '7'),
                         Card('Diamonds', '8'),
                         Card('Diamonds', '9'),
                         Card('Diamonds', '10'),
                         Card('Diamonds', 'Queen'),
                         Card('Diamonds', 'Jack'),
                         Card('Diamonds', 'Ace'),
                         Card('Diamonds', 'King')]

        player2.cards = [Card('Clubs', 'Ace'),
                         Card('Clubs', '10'),
                         Card('Clubs', '8'),
                         Card('Clubs', 'Jack'),
                         Card('Clubs', '7'),
                         Card('Clubs', 'Queen'),
                         Card('Clubs', 'King'),
                         Card('Clubs', '9')]

        player3.cards = [Card('Spades', 'King'),
                         Card('Spades', '8'),
                         Card('Spades', 'Ace'),
                         Card('Spades', '10'),
                         Card('Spades', 'Jack'),
                         Card('Spades', 'Queen'),
                         Card('Spades', '7'),
                         Card('Spades', '9'),
                         ]

        player4.cards = [Card('Hearts', '8'),
                         Card('Hearts', '9'),
                         Card('Hearts', '10'),
                         Card('Hearts', 'Jack'),
                         Card('Hearts', '7'),
                         Card('Hearts', 'Ace'),
                         Card('Hearts', 'Queen'),
                         Card('Hearts', 'King')
                         ]
        new_round.start_player_announcements()
        new_round.check_teams_for_quarte()

        self.assertEqual(len(player1.round_report), 2)
        self.assertEqual(len(player2.round_report), 1)
        self.assertEqual(len(player3.round_report), 1)
        self.assertEqual(len(player4.round_report), 1)

    def test_check_teams_for_tierce_when_two_teams_have_tierce_remove_weaker_tierce(self):
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

        new_round = Round("Diamonds", ordered_players, 1)
        new_round.add_round_members([team1, team2])

        list_of_deck = new_round.make_deck_to_four_decks(new_deck)

        new_round._add_player_cards(list_of_deck)

        player1.cards = [Card('Diamonds', '7'),
                         Card('Diamonds', '8'),
                         Card('Diamonds', '9'),
                         Card('Diamonds', 'Queen'),
                         Card('Diamonds', '10'),
                         Card('Diamonds', 'Jack'),
                         Card('Diamonds', 'Ace'),
                         Card('Diamonds', 'King')]

        player2.cards = [Card('Clubs', 'Ace'),
                         Card('Clubs', '10'),
                         Card('Clubs', '8'),
                         Card('Clubs', 'Jack'),
                         Card('Clubs', '7'),
                         Card('Clubs', 'Queen'),
                         Card('Clubs', 'King'),
                         Card('Clubs', '9')]

        player3.cards = [Card('Spades', 'King'),
                         Card('Spades', '8'),
                         Card('Spades', 'Ace'),
                         Card('Spades', '10'),
                         Card('Spades', 'Queen'),
                         Card('Spades', '7'),
                         Card('Spades', 'Jack'),
                         Card('Spades', '9'),
                         ]

        player4.cards = [Card('Hearts', '8'),
                         Card('Hearts', '9'),
                         Card('Hearts', '10'),
                         Card('Hearts', '7'),
                         Card('Hearts', 'Ace'),
                         Card('Hearts', 'Queen'),
                         Card('Hearts', 'Jack'),
                         Card('Hearts', 'King')
                         ]
        new_round.start_player_announcements()
        new_round.check_teams_for_tierce()

        self.assertEqual(len(player1.round_report), 2)
        self.assertEqual(len(player2.round_report), 1)
        self.assertEqual(len(player3.round_report), 1)
        self.assertEqual(len(player4.round_report), 1)

    def test_check_teams_for_tierce_when_two_teams_have_eq_tierce_remove_both_tierce(self):
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

        new_round = Round("Diamonds", ordered_players, 1)
        new_round.add_round_members([team1, team2])

        list_of_deck = new_round.make_deck_to_four_decks(new_deck)

        new_round._add_player_cards(list_of_deck)

        player1.cards = [Card('Diamonds', '7'),
                         Card('Diamonds', '8'),
                         Card('Diamonds', '9'),
                         Card('Diamonds', 'Queen'),
                         Card('Diamonds', '10'),
                         Card('Diamonds', 'Jack'),
                         Card('Diamonds', 'Ace'),
                         Card('Diamonds', 'King')]

        player2.cards = [Card('Clubs', 'Ace'),
                         Card('Clubs', '10'),
                         Card('Clubs', '8'),
                         Card('Clubs', 'Jack'),
                         Card('Clubs', '7'),
                         Card('Clubs', 'Queen'),
                         Card('Clubs', 'King'),
                         Card('Clubs', '9')]

        player3.cards = [Card('Spades', 'King'),
                         Card('Spades', '8'),
                         Card('Spades', 'Ace'),
                         Card('Spades', '10'),
                         Card('Spades', 'Queen'),
                         Card('Spades', '7'),
                         Card('Spades', 'Jack'),
                         Card('Spades', '9'),
                         ]

        player4.cards = [Card('Hearts', '7'),
                         Card('Hearts', '8'),
                         Card('Hearts', '9'),
                         Card('Hearts', 'Ace'),
                         Card('Hearts', 'Queen'),
                         Card('Hearts', 'Jack'),
                         Card('Hearts', 'King'),
                         Card('Hearts', '10')
                         ]
        new_round.start_player_announcements()
        new_round.check_teams_for_tierce()

        self.assertEqual(len(player1.round_report), 1)
        self.assertEqual(len(player2.round_report), 1)
        self.assertEqual(len(player3.round_report), 1)
        self.assertEqual(len(player4.round_report), 1)


if __name__ == '__main__':
    unittest.main()
