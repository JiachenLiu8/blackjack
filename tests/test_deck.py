import unittest
import math
from src.deck import Deck
from src.card import Card
from src.player import Player

class TestDeck(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()
    
    def test_constructor(self):
        '''
            Test the following fields inside the constructor:
                self._cards  
                self._idx_of_next_card_to_issue 
        '''
        cards = []
        for face_value in range(2, 11):
            for suit in ['club','diamond','heart','spade']:
                cards.append(Card(str(face_value), suit))
        for face_value in ['J','Q','K','A']:
            for suit in ['club','diamond','heart','spade']:
                cards.append(Card(face_value, suit))    
        self.assertEqual(self.deck._cards, cards)
        self.assertEqual(self.deck._idx_of_next_card_to_issue, 0)
        
    def test_swap_card(self):
        '''
            Test if two cards are swapped correctly given their indices.
        '''
        card1 = self.deck._cards[1]
        card2 = self.deck._cards[30]
        self.deck._swap_card(1,30)
        self.assertEqual(self.deck._cards[1], card2)
        self.assertEqual(self.deck._cards[30], card1)
        
    def test_shuffle_card(self):
        '''
            Test if cards are randomly shuffled by checking if all permutations are equally possible.
        '''
        self.deck._cards = []
        for face_value in range(2, 4):
            for suit in ['club','diamond']:
                self.deck._cards.append(Card(str(face_value), suit))
        for face_value in ['J','A']:
            for suit in ['heart','spade']:
                self.deck._cards.append(Card(face_value, suit))
        total_permutations = math.factorial(len(self.deck._cards))
        permutation_counter = {}            
        for trial in range(int(1e5)):
            self.deck.shuffle_cards()
            cards_tuple = tuple(str(card) for card in self.deck._cards)
            permutation_counter[cards_tuple] = permutation_counter.get(cards_tuple, 0) + 1
            #  Important: list is mutable and hence unhashable. Tuple is mutable and hashable.
            #  Custom objects are not hashable. Use their string representation instead.
        for count in permutation_counter.values():    
            self.assertAlmostEqual(count // int(1e5), 1/total_permutations, delta = 0.01)
        for trial in range(int(1e5)):
            self.deck.shuffle_cards()
            cards_tuple = tuple(str(card) for card in self.deck._cards)
            permutation_counter[cards_tuple] = permutation_counter.get(cards_tuple, 0) + 1
            #  Important: list is mutable and hence unhashable. Tuple is mutable and hashable.
            #  Custom objects are not hashable. Use their string representation instead.
        for count in permutation_counter.values():    
            self.assertAlmostEqual(count // int(1e5), 1/total_permutations, delta = 0.01)
    
    def test_issue_card_fail_no_cards_in_initial_deck(self):
        '''
            Check if issue_card() raises Exception when there are no cards in the deck.
        '''
        self.deck._cards = []
        with self.assertRaises(Exception):
            self.deck.issue_card(Player('player_id', 0.3))
        self.assertEqual(self.deck._idx_of_next_card_to_issue, 0)
        
            
    def test_issue_card_fail_all_cards_issued(self):
        '''
            Check if issue_card() raises Exception when all cards in deck have been issued.
        '''
        self.deck._idx_of_next_card_to_issue = len(self.deck._cards) 
        with self.assertRaises(Exception):
            self.deck.issue_card(Player('player_id', 0.3))    
        self.assertEqual(self.deck._idx_of_next_card_to_issue, len(self.deck._cards))    
            
    def test_issue_card_one_card_no_prior_handcards_success(self):
        '''
            Test issuing one card successfully and the player had no prior cards.
        '''
        player = Player(player_id = 'player_id', prob_to_draw = 0.3)
        player._cards = []
        card_to_issue = self.deck._cards[self.deck._idx_of_next_card_to_issue]
        self.assertTrue(self.deck.issue_card(player = player, num_cards_to_issue=1))
        self.assertEqual(player._cards[len(player._cards)-1], card_to_issue)
        self.assertEqual(self.deck._idx_of_next_card_to_issue, 1)
        
    def test_issue_card_one_card_with_prior_handcards_success(self):
        '''
            Test issuing one card successfully and the player had prior handcards.
        '''
        player = Player(player_id = 'player_id', prob_to_draw = 0.3)
        player._cards = [Card(face_value = '2', suit = 'club'), Card(face_value = '2', suit = 'diamond')]
        self.deck._idx_of_next_card_to_issue = 2 #  Two cards in the deck are already issued.
        card_to_issue = self.deck._cards[self.deck._idx_of_next_card_to_issue]
        self.assertTrue(self.deck.issue_card(player = player,num_cards_to_issue = 1))
        self.assertEqual(player._cards, [Card(face_value = '2', suit = 'club'), Card(face_value = '2', suit = 'diamond'), card_to_issue])
        self.assertEqual(self.deck._idx_of_next_card_to_issue, 3)
        
    def test_issue_card_multiple_cards_no_prior_handcards_success(self):
        '''
            Test issuing multiple cards successfully and the player had no prior handcards.
        '''
        player = Player(player_id = 'player_id', prob_to_draw = 0.3)
        player._cards = []
        cards_to_issue = self.deck._cards[self.deck._idx_of_next_card_to_issue : self.deck._idx_of_next_card_to_issue+3 ]
        self.assertTrue(self.deck.issue_card(player = player, num_cards_to_issue = 3))
        self.assertEqual(player._cards, cards_to_issue)
        self.assertEqual(self.deck._idx_of_next_card_to_issue, 3)

    def test_issue_card_multiple_cards_with_prior_handcards_success(self):
        '''
            Test issuing multiple cards successfully and the player had prior handcards.
        '''
        player = Player(player_id = 'player_id', prob_to_draw = 0.3)
        player._cards = [Card(face_value = '2', suit = 'club'), Card(face_value = '2', suit = 'diamond')]
        self.deck._idx_of_next_card_to_issue = 2 #  Two cards in the deck are already issued.
        cards_to_issue = self.deck._cards[self.deck._idx_of_next_card_to_issue : self.deck._idx_of_next_card_to_issue+3 ]
        self.assertTrue(self.deck.issue_card(player = player, num_cards_to_issue = 3))
        self.assertEqual(player._cards, [Card(face_value = '2', suit = 'club'), Card(face_value = '2', suit = 'diamond')]+cards_to_issue)  
        self.assertEqual(self.deck._idx_of_next_card_to_issue, 5)
        
    def test_issue_card_success_for_one_card_fail_for_the_next_two_cards_no_prior_handcards(self):
        '''
            Test the scenario of issuing 3 cards and the player had no prior handcards.
            Successful for 1 card, but then all cards issued and hence fail for later 2 cards.
        '''
        player = Player(player_id = 'player_id', prob_to_draw = 0.3) 
        player._cards = []
        self.deck._idx_of_next_card_to_issue = len(self.deck._cards) - 1 #  Only one card is available to be issued.
        with self.assertRaises(Exception):
            self.deck.issue_card(player = player, num_cards_to_issue = 3)
        self.assertEqual(player._cards[len(player._cards)-1], self.deck._cards[len(self.deck._cards)-1])
        self.assertEqual(self.deck._idx_of_next_card_to_issue, len(self.deck._cards))
        
    def test_issue_card_success_for_one_card_fail_for_the_next_two_cards_with_prior_handcards(self):
        '''
            Test the scenario of issuing 3 cards and the player had prior handcards.
            Successful for 1 card, but then all cards issued and hence fail for later 2 cards.
        '''
        player = Player(player_id = 'player_id', prob_to_draw = 0.3) 
        player._cards = [Card(face_value = '2', suit = 'club'), Card(face_value = '2', suit = 'diamond')]
        self.deck._idx_of_next_card_to_issue = len(self.deck._cards) - 1 #  Only one card is available to be issued.
        with self.assertRaises(Exception):
            self.deck.issue_card(player = player, num_cards_to_issue = 3)
        self.assertEqual(player._cards, [Card(face_value = '2', suit = 'club'), Card(face_value = '2', suit = 'diamond'), self.deck._cards[len(self.deck._cards)-1]])
        self.assertEqual(self.deck._idx_of_next_card_to_issue, len(self.deck._cards))    
    
    def test_get_remaining_cards_no_cards_in_the_initial_deck(self):
        '''
            Test get_num_remaining_cards() for an empty initial deck.
        '''
        self.deck._cards = []
        self.assertEqual(self.deck.get_num_remaining_cards(), 0)
        
    def test_get_remaining_cards_all_cards_issued(self):
        '''
            Test get_num_remaining_cards() when all the cards in the deck have been issued.
        '''
        self.deck._idx_of_next_card_to_issue = len(self.deck._cards)
        self.assertEqual(self.deck.get_num_remaining_cards(), 0)
        
    def test_get_remaining_cards_all_cards_issued(self):
        '''
            Test get_num_remaining_cards() when all the cards in the deck have been issued.
        '''
        self.deck._idx_of_next_card_to_issue = len(self.deck._cards)
        self.assertEqual(self.deck.get_num_remaining_cards(), 0)
    
    def test_get_remaining_cards_all_cards_issued(self):
        '''
            Test get_num_remaining_cards() when 2 cards issued and 50 cards remaining.
            Test get_num_remaining_cards() when 11 cards issued and 41 cards remaining.
        '''
        self.deck._idx_of_next_card_to_issue = 2
        self.assertEqual(self.deck.get_num_remaining_cards(), 50)
        self.deck._idx_of_next_card_to_issue = 11
        self.assertEqual(self.deck.get_num_remaining_cards(), 41)
        
    def test_get_remaining_cards_issue_two_cards_success_issue_three_cards_fail(self):
        '''
            Test get_num_remaining_cards() for successively issuing 3 cards.
            The first 2 cards are successfully issued but the 3rd card fails to be issued.
        '''
        self.deck._idx_of_next_card_to_issue = len(self.deck._cards)-2
        with self.assertRaises(Exception):
            self.deck.issue_card(Player(player_id='player_id', prob_to_draw = 0.3), num_cards_to_issue=3)
        self.assertEqual(self.deck.get_num_remaining_cards(), 0)
      
    
        
    
    