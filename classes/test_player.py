import unittest
from player import Player
from CardsBelote import Deck, Card



class TestPlayer(unittest.TestCase):
    def test_when_create_player_then_all_fields_initialized_correctly(self):
        player = Player("Marto")

        self.assertEqual(player.name, "Marto")
        self.assertEqual(player.cards, [])
        self.assertEqual(player.all_points, 0)
    
    def test_a_player_gets_correct_amount_of_cards(self):
        p = Player('Marto')
        d = Deck()
        d.shuffle()
        hand = d._deal(8)

        p.add_cards(hand)

        self.assertEqual(8, p.hand_size())

    def test_sorting_a_hand_works(self):
        p = Player('Marto')
        d = Deck()
        d.shuffle()
        hand = d._deal(8)
        

        p.add_cards(hand)
        p.cards.sort()
        result = all(p.cards[i] <= p.cards[i+1] for i in range(p.hand_size()-1))

        self.assertTrue(result)
        
        



if __name__ == '__main__':
    unittest.main()
