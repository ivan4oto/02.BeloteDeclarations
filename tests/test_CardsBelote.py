import unittest
from classes.CardsBelote import Card, Deck


class TestCardClass(unittest.TestCase):
    def test_string_representation_return_correct_characters(self):
        c = Card('Spades', 'Ace')
        result = str(c)
        self.assertEqual(result, 'As')

    def test_equality_check_works(self):
        c1 = Card('Spades', 'King')
        c2 = Card('Clubs', 'King')
        self.assertEqual(c1, c2)

    def test_greater_than_works(self):
        c1 = Card('Spades', 'Ace')
        c2 = Card('Clubs', '10')
        self.assertGreater(c1, c2)

    def test_less_than_works(self):
        c1 = Card('Spades', 'Ace')
        c2 = Card('Clubs', 'Queen')
        self.assertLess(c2, c1)

class TestDeckClass(unittest.TestCase):    
    def test_deck_has_the_right_amount_of_cards(self):
        d = Deck()
        result = d.get_count()
        self.assertEqual(result, 32)

    def test_deal_returns_the_right_number_of_cards(self):
        d = Deck()
        result = d._deal(4)
        self.assertEqual(len(result), 4)





if __name__ == "__main__":
    unittest.main()