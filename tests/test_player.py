import unittest
from classes.player import Player


class TestPlayer(unittest.TestCase):
    def test_when_create_player_then_all_fields_initialized_correctly(self):
        player = Player("Marto")

        self.assertEqual(player.name, "Marto")
        self.assertEqual(player.cards, [])
        self.assertEqual(player.all_points, 0)


if __name__ == '__main__':
    unittest.main()