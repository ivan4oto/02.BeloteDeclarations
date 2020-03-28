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

    def test_check_for_announcements_finds_carre150(self):
        p = Player('Ivanchoto')
        carreDeck = [Card('Spades', '7'), Card('Spades', '8'), Card('Spades', '9'), Card('Clubs', '9'), Card('Diamonds', '9'), Card('Hearts','9'), Card('Clubs','King'), Card('Spades', 'Ace')]
        p.add_cards(carreDeck)
        p.check_for_announcements()

        self.assertIn(["carre of 9's = 150 points"], p.announcements)


        
        



if __name__ == '__main__':
    unittest.main()
