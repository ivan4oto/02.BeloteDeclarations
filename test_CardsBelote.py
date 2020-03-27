import unittest
from CardsBelote import Card, Deck


class TestCardClass(unittest.TestCase):
    def test_string_representation_return_correct_characters(self):
        c = Card('Spades', 'Ace')
        result = str(c)
        self.assertEqual(result, 'As')

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