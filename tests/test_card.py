import unittest
from src.card import Card

class TestCard(unittest.TestCase):
    def setUp(self) -> None:
        self.card = Card('2','spade')
    
    def test_constructor(self):
        '''
            Test the face_value and suit fields of the constructor.
        '''
        self.assertEqual(self.card._face_value, '2')
        self.assertEqual(self.card._suit, 'spade')
    
    def test_eq_equal(self):
        '''
            Test the __eq__() for comparing two Card objects with same values for their fields.
        '''
        for face_value in Card._VALID_FACE_VALUES:
            for suit in Card._VALID_SUITS:
                self.assertEqual(Card(face_value,suit), Card(face_value,suit))
    
    def test_eq_not_equal(self):
        '''
            Test the __eq__() for comparing two Card objects with different values for their fields.
        '''
        self.assertNotEqual(Card('2','spade'), Card('3','spade'))
        self.assertNotEqual(Card('2','spade'), Card('2','club'))
        self.assertNotEqual(Card('2','spade'), Card('3','club'))
    
    def test_set_face_value_success(self):
        '''
            Test setting the face_value of a card. The operation is successful.
        '''
        for face_value in Card._VALID_FACE_VALUES:
            self.assertTrue(self.card.set_face_value(face_value))
            self.assertEqual(self.card._face_value, face_value)
        
    def test_set_face_value_fail(self):
        '''
            Test setting the face_value of a card. The input face_value is invalid and the operation fails.
        '''
        with self.assertRaises(ValueError):
            self.card.set_face_value('11')
    
    def test_get_face_value_constructor(self):
        '''
            Test the getter for face_value for values assigned via constructor.
        '''
        self.assertEqual(self.card.get_face_value(), '2')
    
    def test_get_face_value_after_setter(self):
        '''
            Test getter for getting face_value from reassignment via setter.
        '''
        for face_value in Card._VALID_FACE_VALUES:
            self.card.set_face_value(face_value)
            self.assertEqual(self.card.get_face_value(), face_value)
        
    def test_set_suit_success(self):
        '''
            Test setting the suit of a card. The operation is successful.
        '''
        for suit in Card._VALID_SUITS:
            self.assertTrue(self.card.set_suit(suit))
            self.assertEqual(self.card._suit, suit)
    
    def test_set_suit_fail(self):
        '''
           Test setting the suit of a card. The input suit is invalid and the operation fails. 
        '''
        with self.assertRaises(ValueError):
            self.card.set_suit('invalid_suit')
        
    def test_get_suit_constructor(self):
        '''
            Test getter for getting suit from constructor.
        '''
        self.assertEqual(self.card.get_suit(), 'spade')
    
    def test_get_suit_after_setter(self):
        '''
            Test getter for getting suit from reassignment via setter.
        '''
        for suit in Card._VALID_SUITS:
            self.card._suit = suit
            self.assertEqual(self.card.get_suit(), suit)
    
    def test_is_face_facecard(self):
        '''
            Test if a facecard (face_value being J, K, Q) is correctly recognized as facecard.
        '''
        for suit in Card._VALID_SUITS:
            card = Card('J',suit) 
            self.assertTrue(card.is_face)
            card = Card('K',suit) 
            self.assertTrue(card.is_face)
            card = Card('Q',suit) 
            self.assertTrue(card.is_face)
        
    def test_is_face_not_facecard(self):
        '''
            Test if a non-facecard (face_value other than J, K, Q) is rejected as a facecard.
        '''
        for suit in Card._VALID_SUITS:
            card = Card('2',suit) 
            self.assertFalse(card.is_face())
            card = Card('A',suit) 
            self.assertFalse(card.is_face())
        
    def test_is_ace_acecard(self):
        '''
            Test if an ace card is correctly recognized as an ace.
        '''
        for suit in Card._VALID_SUITS:
            card = Card('A',suit) 
            self.assertTrue(card.is_ace()) 
        
    def test_is_ace_not_acecard(self):
        '''
            Test is_ace() for a non-ace card. The expected outcome is false.
        '''
        for suit in Card._VALID_SUITS:
            card = Card('2',suit) 
            card = Card('K',suit) 
            self.assertFalse(card.is_ace()) 
        
    def test_score_numeric(self):
        '''
            Test the score() for cards with numeric face_value.
        '''
        for suit in Card._VALID_SUITS:
            card = Card('2',suit)
            self.assertEqual(card.score(), 2)
            card = Card('10',suit)
            self.assertEqual(card.score(), 10)
        
    def test_score_face(self):
        '''
            Test the score() for face cards and check if the are recognized as score 10.
        '''
        for suit in Card._VALID_SUITS:
            card = Card('J',suit)
            card = Card('K',suit)
            card = Card('Q',suit)
            self.assertEqual(card.score(), 10)
    
    def test_score_ace(self):
        '''
            Test the score() for Ace cards. The return value from this function should be -1.
        '''
        for suit in Card._VALID_SUITS:
            card = Card('A',suit)
            self.assertEqual(card.score(), -1)
        
    def test_str_equal(self):
        '''
            Test the __str__() for equal case.
        '''
        card = Card('2', 'diamond')
        self.assertEqual(str(card), f"Card object with face_value={'2'}, suit={'diamond'}")
        card = Card('10', 'club')
        self.assertEqual(str(card), f"Card object with face_value={'10'}, suit={'club'}")
        card = Card('J', 'diamond')
        self.assertEqual(str(card), f"Card object with face_value={'J'}, suit={'diamond'}")
        card = Card('A', 'spade')
        self.assertEqual(str(card), f"Card object with face_value={'A'}, suit={'spade'}")
        
    def test_str_not_equal(self):
        '''
            Test the __str__() for not equal case.
        '''
        card = Card('2', 'diamond')
        self.assertNotEqual(str(card), f"Card object with face_value={'3'}, suit={'diamond'}")
        card = Card('10', 'club')
        self.assertNotEqual(str(card), f"Card object with face_value={'10'}, suit={'heart'}")
        card = Card('J', 'diamond')
        self.assertNotEqual(str(card), f"Card object with face_value={'K'}, suit={'diamond'}")
        card = Card('A', 'spade')
        self.assertNotEqual(str(card), f"Card object with face_value={'A'}, suit={'heart'}")
        
    def test_gt_success(self):
        '''
            Test the __gt__() for the return value of card A > card B when A's face_value is greater then B's face_value.
        '''
        self.assertGreater(Card('2', 'diamond'), Card('A', 'diamond'))
        self.assertGreater(Card('5', 'diamond'), Card('2', 'diamond'))
        self.assertGreater(Card('J', 'diamond'), Card('10', 'diamond'))
        self.assertGreater(Card('K', 'diamond'), Card('Q', 'diamond'))
        
    def test_gt_fail(self):
        '''
            Test the __gt__() for the return value of card A > card B when A's face_value is not greater then B's face_value.
        '''
        self.assertFalse(Card('A', 'diamond') > Card('2', 'diamond'))
        self.assertFalse(Card('3', 'diamond') > Card('4', 'diamond'))
        self.assertFalse(Card('10', 'diamond')> Card('10', 'diamond'))
        self.assertFalse(Card('10', 'diamond')> Card('J', 'diamond'))
        self.assertFalse(Card('J', 'diamond')> Card('K', 'diamond'))
        self.assertFalse(Card('Q', 'diamond')> Card('K', 'diamond'))
      
    def test_lt_success(self):
        '''
            Test the __lt__() for the return value of card A < card B when A's face_value is smaller then B's face_value.
        '''
        self.assertLess(Card('A', 'diamond'), Card('2', 'diamond'))
        self.assertLess(Card('5', 'diamond'), Card('7', 'diamond'))
        self.assertLess(Card('10', 'diamond'), Card('J', 'diamond'))
        self.assertLess(Card('Q', 'diamond'), Card('K', 'diamond'))
        
    def test_lt_fail(self):
        '''
            Test the __lt__() for the return value of card A < card B when A's face_value is not smaller then B's face_value.
        '''
        self.assertFalse(Card('2', 'diamond') < Card('A', 'diamond'))
        self.assertFalse(Card('4', 'diamond') < Card('3', 'diamond'))
        self.assertFalse(Card('10', 'diamond')< Card('10', 'diamond'))
        self.assertFalse(Card('Q', 'diamond') < Card('J', 'diamond'))
        
    def test_ge_success(self):
        '''
            Test A >= B for successful cases.
        '''
        self.assertGreaterEqual(Card('2', 'diamond'), Card('A', 'diamond'))
        self.assertGreaterEqual(Card('A', 'diamond'), Card('A', 'diamond'))
    
    def test_ge_fail(self):
        '''
            Test A >= B for failure cases.
        '''
        self.assertFalse(Card('A', 'diamond') >= Card('3', 'diamond'))
      
    def test_le_success(self):
        '''
            Test A <= B for successful cases.
        '''
        self.assertLessEqual(Card('2', 'diamond'), Card('3', 'diamond'))
        self.assertLessEqual(Card('A', 'diamond'), Card('A', 'diamond'))
        
    def test_le_fail(self):
        '''
            Test A <= B for failure cases.
        '''
        self.assertFalse(Card('3', 'diamond') <= Card('A', 'diamond'))