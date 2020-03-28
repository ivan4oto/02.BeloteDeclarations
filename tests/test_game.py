import unittest
from classes.player import Player
from classes.team import Team
from classes.game import Game


class TestGame(unittest.TestCase):
    def test_create_new_game(self):
        player1 = Player("Marto")
        player2 = Player("Pesho")
        player3 = Player("Nasko")
        player4 = Player("Petko")

        team1 = Team("Wolf")
        team2 = Team("Lion")
        team1.add_team_members([player1, player2])
        team2.add_team_members([player3, player4])

        game = Game([team1, team2], 1)

        self.assertEqual(game.rounds, [])
        self.assertEqual(game.game_number, 1)
        self.assertEqual(game.winner,False)
        self.assertEqual(game.current_round, 1)



if __name__ == '__main__':
    unittest.main()
