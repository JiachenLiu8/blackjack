from src.player import Player, Dealer
from src.card import Card
from src.deck import Deck
from src.game import Game
import math
import random
import unittest


def initialize_deck_for_testcase(deck: Deck):
        '''
            A helper function for initializing the deck in a specific order.
            Face values are in order 2-11 and J,Q,K,A and each value's suits are in order club, diamond, heart, spade
        '''
        deck._cards = []
        for face_value in range(2, 11):
            for suit in ['club','diamond','heart','spade']:
                deck._cards.append(Card(str(face_value), suit))
        for face_value in ['J','Q','K','A']:
            for suit in ['club','diamond','heart','spade']:
                deck._cards.append(Card(face_value, suit))
        deck._idx_of_next_card_to_issue = 0
        
def initialize_deck_for_testcase_start_from_ace(deck: Deck):
        '''
            A helper function for initializing the deck in a specific order.
            Face values are in order 2-11 and J,Q,K,A and each value's suits are in order club, diamond, heart, spade
        '''
        deck._cards = []
        for suit in ['club','diamond','heart','spade']:
                deck._cards.append(Card('A', suit))
        for face_value in range(2, 11):
            for suit in ['club','diamond','heart','spade']:
                deck._cards.append(Card(str(face_value), suit))
        for face_value in ['J','Q','K']:
            for suit in ['club','diamond','heart','spade']:
                deck._cards.append(Card(face_value, suit))
        deck._idx_of_next_card_to_issue = 0

class TestGame(unittest.TestCase):
    # def setUp(self):
        
    #     '''
    #         Construct a game object with: 
    #             1 dealer with 0.3 probability of drawing a card
    #             And 2 players with 0.4 and 0.5 probability of drawing a card.
    #     '''
    #     game = Game(('dealer', 0.3),[('player1', 0.4), ('player2', 0.5)])
      
    def test_constructor(self):
        '''
            Test the following fields in the constructor:
                self._turn_number 
                self._deck
                self._dealer
                self._players
        '''
        # Construct a game object with 1 dealer with 0.3 probability of drawing a card and 2 players with 0.4 and 0.5 probability of drawing a card.
        game = Game(('dealer', 0.3),[('player1', 0.4), ('player2', 0.5)])
        self.assertEqual(game._turn_number, 0)
        self._deck = Deck()
        self.assertEqual(game._dealer, Dealer(player_id = 'dealer', prob_to_draw = 0.3))
        self.assertEqual(game._players, [Player(player_id = 'player1', prob_to_draw = 0.4), Player(player_id = 'player2', prob_to_draw = 0.5)])

    def test_str_(self):
        '''
            Test the toString method.
        '''
        game = Game(('dealer', 0.3),[('player1', 0.4), ('player2', 0.5)])
        self.assertEqual(
                str(game),
                f"Game object with number of players: {2}, "
                f"current turn number: {0}, "
                f"available card pool: {[ str(card) for card in game._deck._cards]}, "
                f"dealer: {str(game._dealer)}"
                f"players: {[str(player) for player in game._players]}"
                )
        
    def test_print_essential_info(self):
        '''
            Test the print_essential_info().
        '''
        game = Game(('dealer', 0.3),[('player1', 0.4), ('player2', 0.5)])
        self.assertEqual(game.print_essential_info(), (f'Game with {2} players, current turn number is {0}'))
        
    def test_get_turn_number_constructor(self):
        '''
            Test get_turn_number() for turn number field assigend via constructor.
        '''
        # Construct a game object with 1 dealer with 0.3 probability of drawing a card and 2 players with 0.4 and 0.5 probability of drawing a card.
        game = Game(('dealer', 0.3),[('player1', 0.4), ('player2', 0.5)])
        self.assertEqual(game.get_turn_number(), 0)
        
    def test_get_turn_number_after_reassignment(self):
        '''
            Test get_turn_number() for turn number field after reassignment.
        '''
        # Construct a game object with 1 dealer with 0.3 probability of drawing a card and 2 players with 0.4 and 0.5 probability of drawing a card.
        game = Game(('dealer', 0.3),[('player1', 0.4), ('player2', 0.5)])
        game._turn_number = 3
        self.assertEqual(game.get_turn_number(), 3)
        
    def test_assign_initial_two_cards_fail_initial_deck_empty(self):
        '''
            Test assign_initial_two_cards() for an empty initial deck.
        '''
        # Construct a game object with 1 dealer with 0.3 probability of drawing a card and 2 players with 0.4 and 0.5 probability of drawing a card.
        game = Game(('dealer', 0.3),[('player1', 0.4), ('player2', 0.5)])
        game._deck._cards = []
        with self.assertRaises(Exception):
            self.deck.assign_initial_two_cards()
                      
    def test_assign_initial_two_cards_fail_player_numbers_over_max(self):
        '''
            Test assign_initial_two_cards() when number of players over max (1 dealer + 25 players).
        '''
        # Construct a game object with 1 dealer with 0.3 probability of drawing a card and 2 players with 0.4 and 0.5 probability of drawing a card.
        game = Game(('dealer', 0.3),[('player1', 0.4), ('player2', 0.5)])
        players = [Player(f'player{i}', 0.4) for i in range(26)] #  A list of tuples of player ids and player's probability to draw a card.
        game._players = players
        with self.assertRaises(Exception):
            game.assign_initial_two_cards()
        
    def test_assign_initial_two_cards_success(self):
        '''
            Test assign_initial_two_cards() when the operation is successful.
        '''
        # Construct a game object with 1 dealer with 0.3 probability of drawing a card and 2 players with 0.4 and 0.5 probability of drawing a card.
        game = Game(('dealer', 0.3),[('player1', 0.4), ('player2', 0.5)])
        initialize_deck_for_testcase(game._deck)
        self.assertTrue(game.assign_initial_two_cards())
        self.assertEqual(game._dealer._cards, [Card(face_value='2', suit='club'), Card(face_value='2', suit='diamond') ])
        self.assertEqual(game._players[0]._cards, [Card(face_value='2', suit='heart'), Card(face_value='2', suit='spade') ])
        self.assertEqual(game._players[1]._cards, [Card(face_value='3', suit='club'), Card(face_value='3', suit='diamond') ])
             
    def test_run_dealer_turn_initial_score_below_17_busted_after_one_draw_due_to_forced_draw(self):
        '''
            Dealer's initial score is below 17 and must draw cards. After drawing one card the dealer is busted.
        '''
        # Construct a game object with 1 dealer and 13 players, each has 0.3 probability of drawing a card.
        players_info = [(f'player{i}', 0.3) for i in range(13)]
        game = Game(dealer_info=('dealer', 0.3), players_info=players_info)
        initialize_deck_for_testcase(game._deck)
        game._deck._swap_card(0, 20)  # Swap the order of Card(face_value='2', suit='club') and Card(face_value='7', suit='club')
        game._deck._swap_card(1, 21)  # Swap the order of Card(face_value='2', suit='diamond') and Card(face_value='7', suit='diamond')
        game._dealer._cards = [Card(face_value='7', suit='club'), Card(face_value='7', suit='diamond')]
        game._deck._idx_of_next_card_to_issue = 28  # Next card to issue is Card(face_value='9', suit='club')
        self.assertTrue(game.run_dealer_turn())
        self.assertEqual(game._dealer.calculate_score(), -1)   
        self.assertEqual(game._dealer._cards, [Card(face_value='7', suit='club'), Card(face_value='7', suit='diamond'), Card(face_value='9', suit='club')])
        self.assertEqual(game._deck._idx_of_next_card_to_issue, 29)
              
    def test_run_dealer_turn_initial_score_below_17_busted_after_three_draws_due_to_force_draws(self):
        '''
            Dealer's initial score is below 17 and must draw cards. After drawing 3 cards the dealer is busted.
        '''
        # Construct a game object with 1 dealer with 0.3 probability of drawing a card.
        players_info = [(f'player{i}', 0.3) for i in range(7)]
        game = Game(dealer_info = ('dealer', 0.3), players_info = players_info)
        initialize_deck_for_testcase(game._deck)
        game._dealer._cards = [Card(face_value='2', suit='club'), Card(face_value='2', suit='diamond')]
        game._deck._idx_of_next_card_to_issue = 16  # Next card to issue is Card(face_value='6', suit='club')
        self.assertTrue(game.run_dealer_turn())
        self.assertEqual(game._dealer.calculate_score(), -1)   
        self.assertEqual(game._dealer._cards, [Card(face_value='2', suit='club'), Card(face_value='2', suit='diamond'), Card(face_value='6', suit='club'), Card(face_value='6', suit='diamond'), Card(face_value='6', suit='heart')])
        self.assertEqual(game._deck._idx_of_next_card_to_issue, 19)
                  
    def test_run_dealer_turn_initial_score_below_17_not_busted(self):
        '''
            Dealer's initial score is below 17 and must draw cards. After drawing 3 cards the dealer is still not busted and the score >= 17 and decide not to draw.
        '''
        # Construct a game object with 1 dealer with 0.3 probability of drawing a card.
        game = Game(('dealer', 0.3),[('player1', 0.4), ('player2', 0.5)])
        initialize_deck_for_testcase(game._deck)
        # Further adjust the deck order so that facevalues are in order: 3,3,2,2,3,3,4,7,2,2,4,4,5,5,5,5,6,6,6,6,7,4,7,7,... via the following 5 swaps
        game._deck._swap_card(0, 6)  # Swap the order of Card(face_value='2', suit='club') and Card(face_value='3', suit='heart')
        game._deck._swap_card(1, 7)  # Swap the order of Card(face_value='2', suit='diamond') and Card(face_value='3', suit='spade')
        game._deck._swap_card(6, 8)  # Swap the order of Card(face_value='2', suit='club') and Card(face_value='4', suit='club')
        game._deck._swap_card(7, 9)  # Swap the order of Card(face_value='2', suit='diamond') and Card(face_value='4', suit='diamond')
        game._deck._swap_card(7, 21)  # Swap the order of Card(face_value='4', suit='diamond') and Card(face_value='7', suit='diamond')
        num_trials = int(1e7)
        case1_counter = 0  # Case1: handcards: 3,3, drawing 4,7
        case2_counter = 0  # Case2: handcards: 3,3, drawing 4,7,2
        case3_counter = 0  # Case3: handcards: 3,3, drawing 4,7,2,2
        for trial in range(num_trials):
            game._dealer._cards = [Card(face_value='3', suit='heart'), Card(face_value='3', suit='spade')]
            game._deck._idx_of_next_card_to_issue = 6  # Next card to issue is Card(face_value='4', suit='club')
            game.run_dealer_turn()
            self.assertGreaterEqual(game._deck._idx_of_next_card_to_issue, 8)  # Must draw at least two cards to achieve score 17 before being able to stop drawing.
            # 3 possible cases after achieving 17: no more draws; drawing 2 and stop; drawing 2,2 and stop.
            if game._deck._idx_of_next_card_to_issue == 8 and game._dealer._cards == [Card(face_value='3', suit='heart'), Card(face_value='3', suit='spade'), Card(face_value='4', suit='club'), Card(face_value='7', suit='diamond')]:
                case1_counter += 1
            elif game._deck._idx_of_next_card_to_issue == 9 and game._dealer._cards == [Card(face_value='3', suit='heart'), Card(face_value='3', suit='spade'), Card(face_value='4', suit='club'), Card(face_value='7', suit='diamond'),Card(face_value='2', suit='club') ]:
                case2_counter += 1
            elif game._deck._idx_of_next_card_to_issue == 10 and game._dealer._cards == [Card(face_value='3', suit='heart'), Card(face_value='3', suit='spade'), Card(face_value='4', suit='club'), Card(face_value='7', suit='diamond'), Card(face_value='2', suit='club'), Card(face_value='2', suit='diamond')]:
                case3_counter += 1
        p_success = 1 - game._dealer._prob_to_draw
        self.assertAlmostEqual(case1_counter/num_trials,(1-p_success)**(1-1)*p_success, delta = 1e-4)
        self.assertAlmostEqual(case2_counter/num_trials,(1-p_success)**(2-1)*p_success, delta = 1e-4)
        self.assertAlmostEqual(case3_counter/num_trials,(1-p_success)**(3-1)*p_success, delta = 1e-4)
    
    def test_run_dealer_turn_initial_score_below_17_not_busted_test_large_number_of_handcards(self):
        '''
            Dealer's initial score is below 17 and must draw cards. 
            After drawing multiple cards the dealer is still not busted and the score >= 17 and decide not to draw.
            Test large number of handcards as an extreme case.
        '''
        # Construct a game object with 1 dealer with 0.3 probability of drawing a card.
        game = Game(('dealer', 0.3),[('player1', 0.4)])
        game._deck._cards = []
        initialize_deck_for_testcase_start_from_ace(game._deck)
        #  Further adjust deck order to achieve deck order: A,A,3,3,A,A,2,2,2,2,4,4,4,4,...
        game._deck._swap_card(2,8)  # Swap the order of Card(face_value='A', suit='heart') and Card(face_value='3', suit='club')
        game._deck._swap_card(3,9)  # Swap the order of Card(face_value='A', suit='spade') and Card(face_value='3', suit='diamond')
        game._deck._swap_card(4,8)  # Swap the order of Card(face_value='2', suit='club') and Card(face_value='A', suit='heart')
        game._deck._swap_card(5,9)  # Swap the order of Card(face_value='2', suit='diamond') and Card(face_value='A', suit='spade')
        final_handcards = [Card(face_value='A', suit='club'),
                           Card(face_value='A', suit='diamond'),
                           Card(face_value='A', suit='heart'),
                           Card(face_value='A', suit='spade'),
                           Card(face_value='2', suit='heart'),
                           Card(face_value='2', suit='spade'),
                           Card(face_value='2', suit='club'),
                           Card(face_value='2', suit='diamond'),
                           Card(face_value='3', suit='spade'),
                           Card(face_value='3', suit='spade')]
        case_counter = 0  # Case: handcards A,A, final handcards as listed above.
        num_trials = int(1e7)
        for trial in range(num_trials): 
            game._dealer._cards = [Card(face_value='A', suit='club'), Card(face_value='A', suit='diamond')]
            game._deck._idx_of_next_card_to_issue = 4  # Next card to issue is Card(face_value='A', suit='heart')
            game.run_dealer_turn()
            self.assertGreaterEqual(game._deck._idx_of_next_card_to_issue, 8) #  Initial handcards are A,A. At least has to further draw A,A,2,2 to achieve score >= 17.
            if game._deck._idx_of_next_card_to_issue == 14 and game._dealer._cards == final_handcards:
                case_counter += 1
                self.assertEqual(game._dealer.calculate_score(), 18)
        p_success = 1 - game._dealer._prob_to_draw
        self.assertAlmostEqual(case_counter/num_trials,(1-p_success)** 6 * p_success, delta = 1e-4)
       
                
    def test_run_dealer_turn_initial_score_below_17_busted_due_to_optional_draws(self):
        '''
            Dealer's initial score is below 17 and must draw cards. After drawing multiple cards the dealer is still not busted and the score >= 17 but then get busted after further optional draws.
        '''
        # Construct a game object with 1 dealer with 0.3 probability of drawing a card.
        game = Game(('dealer', 0.3),[('player1', 0.4), ('player2', 0.5)])
        initialize_deck_for_testcase(game._deck)
        # Further adjust the deck order so that facevalues are in order: 3,3,2,2,3,3,4,7,2,2,4,4,5,5,5,5,6,6,6,6,7,4,7,7,... via the following 5 swaps
        game._deck._swap_card(0, 6)  # Swap the order of Card(face_value='2', suit='club') and Card(face_value='3', suit='heart')
        game._deck._swap_card(1, 7)  # Swap the order of Card(face_value='2', suit='diamond') and Card(face_value='3', suit='spade')
        game._deck._swap_card(6, 8)  # Swap the order of Card(face_value='2', suit='club') and Card(face_value='4', suit='club')
        game._deck._swap_card(7, 9)  # Swap the order of Card(face_value='2', suit='diamond') and Card(face_value='4', suit='diamond')
        game._deck._swap_card(7, 21)  # Swap the order of Card(face_value='4', suit='diamond') and Card(face_value='7', suit='diamond')
        num_trials = int(1e7)
        case_counter = 0  # Case: handcards: 3,3, drawing 4,7,2,2,4
        for trial in range(num_trials):
            game._dealer._cards = [Card(face_value='3', suit='heart'), Card(face_value='3', suit='spade')]
            game._deck._idx_of_next_card_to_issue = 6  # Next card to issue is Card(face_value='4', suit='club')
            game.run_dealer_turn()
            self.assertGreaterEqual(game._deck._idx_of_next_card_to_issue, 8)  # Must draw at least two cards to achieve score 17 before being able to stop drawing.
            self.assertLessEqual(game._deck._idx_of_next_card_to_issue, 11)  # The dealer will bust after drawing 5 cards.
            if game._deck._idx_of_next_card_to_issue == 11 and game._dealer._cards == [Card(face_value='3', suit='heart'), Card(face_value='3', suit='spade'), Card(face_value='4', suit='club'), Card(face_value='7', suit='diamond'), Card(face_value='2', suit='club'), Card(face_value='2', suit='diamond'), Card(face_value='4', suit='heart')]:
                case_counter += 1
                self.assertEqual(game._dealer.calculate_score(), -1)
        p_success = 1 - game._dealer._prob_to_draw
        self.assertAlmostEqual(case_counter/num_trials,(1-p_success)** 3, delta = 1e-4)
              
    
    # def test_run_player_turn_busted_during_run(self):
        
    
    # def test_run_player_turn_not_busted(self):
    
    
    def test_blackjacks(self):
        '''
            Test get_blackjacks() when there are blackjacks.
        '''
        game = Game(dealer_info=('dealer', 0.3), players_info=[('player1', 0.4), ('player2', 0.5)])
        game._dealer._cards = [Card(face_value='A',suit = 'club'), Card(face_value='10', suit = 'club')]
        game._players[0]._cards = [Card(face_value='A',suit = 'heart'), Card(face_value='A', suit = 'spade')]
        game._players[0]._cards = [Card(face_value='10',suit = 'heart'), Card(face_value='10', suit = 'spade')]
        print([str(player) for player in game.get_blackjacks()])
        # self.assertEqual(game.get_blackjacks(), [Dealer(player_id='dealer',prob_to_draw=0.3)])
    
    
                 
        
        
        
    
    

