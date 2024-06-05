import unittest
from src.player import Player, Dealer
from src.card import Card

class TestPlayer(unittest.TestCase):
    def setUp(self):
        '''
            Construct player object
        '''
        self.player = Player('player_id', 0.3)
        self.dealer = Dealer('dealer_id', 0.4)
        
    def test_constructor(self):
        '''
            Test all fields inside the constructor.
        '''
        self.assertEqual(self.player._player_id, 'player_id')
        self.assertEqual(self.player._cards, [])
        self.assertEqual(self.player._score, 0)
        self.assertEqual(self.player._prob_to_draw, 0.3)
        
    def test_calculate_score_no_ace_two_handcards_not_busted(self):
       '''
           Check score calculation when there are no Ace cards at hand. There are a total of two cards at hand.
           The player is not busted.
       '''
       self.player._cards = [Card('5','diamond'), Card('7','heart')]
       self.assertEqual(self.player.calculate_score(),12)
    
    def test_calculate_score_no_ace_four_handcards_not_busted(self):
        '''
            Check score calculation when no ace cards and a total of four cards at hand. 
            The player is not busted.
        '''
        self.player.set_cards([Card('2','diamond'), Card('2','heart'), Card('3','spade'), Card('5','club')])
        self.assertEqual(self.player.calculate_score(),12)
    
    def test_calculate_score_no_ace_six_handcards_not_busted(self):
        '''
            Check score calculation when no Ace cards and a total of six cards at hand. 
            The player is not busted.
        '''
        self.player.set_cards([Card('2','diamond'), Card('2','heart'), Card('3','spade'), Card('3','club'), Card('3','diamond'), Card('4','heart')])
        self.assertEqual(self.player.calculate_score(),17)
    
    def test_calculate_score_zero_Ace_three_handcards_busted(self):
        '''
            Check score calculation when no Ace cards and a toal of two cards at hand.
            Busted.
        '''
        self.player.set_cards([Card('2','diamond'), Card('10','heart'), Card('10','spade')])
        self.assertEqual(self.player.calculate_score(),-1)
    
    def test_calculate_score_zero_Ace_four_handcards_busted(self):
        '''
            Check score calculation when no Ace cards and a toal of four cards at hand.
            Busted.
        '''
        self.player.set_cards([Card('2','diamond'), Card('3','diamond'), Card('10','heart'), Card('10','spade')])
        self.assertEqual(self.player.calculate_score(),-1) 
        
    def test_calculate_score_zero_Ace_six_handcards_busted(self):
        '''
            Check score calculation when no Ace cards and a toal of six cards at hand.
            Busted.
        '''
        self.player.set_cards([Card('2','diamond'), Card('3','diamond'),  Card('4','diamond'),  Card('5','diamond'), Card('10','heart'), Card('10','spade')])
        self.assertEqual(self.player.calculate_score(),-1) 
    
    def test_calculate_score_one_Ace_treat_as_one_total_three_handcards_not_busted(self):
        '''
            Check score calculation when one Ace card.
            The Ace card is treated as one.
            Total three cards at hand.
            Total score <= 21. Not busted.
        '''
        self.player.set_cards([Card('10','diamond'), Card('10','heart'), Card('A','spade')])
        self.assertEqual(self.player.calculate_score(),21)    
        
    def test_calculate_score_one_Ace_treat_as_one_total_four_handcards_not_busted(self):
        '''
            Check score calculation when one Ace card.
            The Ace card is treated as one.
            Total four cards at hand.
            Total score <= 21. Not busted.
        '''
        self.player.set_cards([Card('2','diamond'), Card('7','diamond'), Card('10','heart'), Card('A','spade')])
        self.assertEqual(self.player.calculate_score(),20)    
    
    def test_calculate_score_one_Ace_treat_as_one_total_six_handcards_not_busted(self):
        '''
            Check score calculation when one Ace card.
            The Ace card is treated as one.
            Total six cards at hand.
            Total score <= 21. Not busted.
        '''
        self.player.set_cards([Card('2','diamond'), Card('3','diamond'), Card('4','diamond'), Card('5','heart'),Card('5','spade'), Card('A','spade')])
        self.assertEqual(self.player.calculate_score(),20)  

    def test_calculate_score_one_Ace_treat_as_eleven_total_two_handcards_not_busted(self):
        '''
            Check score calculation when one Ace card.
            The Ace card is treated as eleven.
            Total two cards at hand.
            Total score <= 21. Not busted.
        '''
        self.player.set_cards([Card('9','diamond'), Card('A','spade')])
        self.assertEqual(self.player.calculate_score(),20)
        
    def test_calculate_score_one_Ace_treat_as_eleven_total_two_handcards_not_busted(self):
        '''
            Check score calculation when one Ace card.
            The Ace card is treated as eleven.
            Total two cards at hand.
            Total score <= 21. Not busted.
        '''
        self.player.set_cards([Card('9','diamond'), Card('A','spade')])
        self.assertEqual(self.player.calculate_score(),20)  
    
    def test_calculate_score_one_Ace_treat_as_eleven_total_four_handcards_not_busted(self):
        '''
            Check score calculation when one Ace card.
            The Ace card is treated as eleven.
            Total four cards at hand.
            Total score <= 21. Not busted.
        '''
        self.player.set_cards([Card('A','diamond'), Card('3','spade'), Card('3','heart'), Card('3','club')])
        self.assertEqual(self.player.calculate_score(),20)    
      
    def test_calculate_score_one_Ace_treat_as_eleven_total_five_handcards_not_busted(self):
        '''
            Check score calculation when one Ace card.
            The Ace card is treated as eleven.
            Total five cards at hand.
            Total score <= 21. Not busted.
        '''
        self.player.set_cards([Card('A','diamond'), Card('2','spade'), Card('2','heart'), Card('2','club'), Card('2','diamond')])
        self.assertEqual(self.player.calculate_score(), 19)    
        
   
    def test_calculate_score_one_Ace_total_four_handcards_busted(self):
        '''
            Check score calculation when one Ace card.
            Total two cards at hand.
            Busted.
        '''
        self.player.set_cards([Card('5','diamond'), Card('5','spade'), Card('5','heart'), Card('6','club'), Card('A','spade')])
        self.assertEqual(self.player.calculate_score(), -1)
                 
    def test_calculate_score_one_Ace_total_six_handcards_busted(self):
        '''
            Check score calculation when one Ace card.
            Total six cards at hand.
            Busted.
        '''
        self.player.set_cards([Card('2','diamond'), Card('3','diamond'), Card('4','diamond'), Card('6','heart'),Card('6','spade'), Card('A','spade')])
        self.assertEqual(self.player.calculate_score(),-1)  
        
   
    #  Two Aces.    
    def test_calculate_score_two_Aces_treated_as_one_and_one_total_three_handcards_not_busted(self):
        '''
            Check score calculation when two Ace cards treated as one and one.
            Total 3 cards at hand.
            Total score <= 21. Not busted.
        '''
        self.player.set_cards([Card('A','diamond'), Card('A','heart'), Card('10','heart')])
        self.assertEqual(self.player.calculate_score(), 12)
        
    def test_calculate_score_two_Aces_treated_as_one_and_one_total_four_handcards_not_busted(self):
        '''
            Check score calculation when two Ace cards treated as one and one.
            Total 4 cards at hand.
            Total score <= 21. Not busted.
        '''
        self.player.set_cards([Card('A','diamond'), Card('A','heart'), Card('9','heart'), Card('10','heart') ])
        self.assertEqual(self.player.calculate_score(), 21)
    
    def test_calculate_score_two_Aces_treated_as_one_and_one_total_six_handcards_not_busted(self):
        '''
            Check score calculation when two Ace cards treated as one and one.
            Total six cards at hand.
            Total score <= 21. Not busted.
        '''
        self.player.set_cards([Card('A','diamond'), Card('A','heart'), Card('3','heart'), Card('6','heart'), Card('5','heart'), Card('5','spade')])
        self.assertEqual(self.player.calculate_score(), 21)
    
    def test_calculate_score_two_Aces_treated_as_one_and_eleven_total_two_handcards_not_busted(self):
        '''
            Check score calculation when two Ace cards treated as 1 and 11.
            Total 2 cards at hand.
            Total score <= 21. Not busted.
        '''
        self.player.set_cards([Card('A','diamond'), Card('A','heart') ])
        self.assertEqual(self.player.calculate_score(), 12)
        
    def test_calculate_score_two_Aces_treated_as_one_and_eleven_total_four_handcards_not_busted(self):
        '''
            Check score calculation when two Ace cards treated as 1 and 11.
            Total 4 cards at hand.
            Total score <= 21. Not busted.
        '''
        self.player.set_cards([Card('A','diamond'), Card('A','heart'), Card('4','heart'), Card('5','heart') ])
        self.assertEqual(self.player.calculate_score(), 21)
    
    def test_calculate_score_two_Aces_treated_as_one_and_eleven_total_six_handcards_not_busted(self):
        '''
            Check score calculation when two Ace cards treated as 1 and 11.
            Total 6 cards at hand.
            Total score <= 21. Not busted.
        '''
        self.player.set_cards([Card('A','diamond'), Card('A','heart'), Card('2','heart'), Card('2','spade'), Card('2','club'), Card('3','spade')])
        self.assertEqual(self.player.calculate_score(), 21)
    
    def test_calculate_score_two_Aces_total_four_handcards_busted(self):
        '''
            Check score calculation when two Ace cards.
            Total 4 cards at hand.
            Busted.
        '''
        self.player.set_cards([Card('A','diamond'), Card('A','heart'), Card('10','spade'), Card('10','heart') ])
        self.assertEqual(self.player.calculate_score(), -1)
    
    def test_calculate_score_two_Aces_total_six_handcards_busted(self):
        '''
            Check score calculation when two Ace cards.
            Total six cards at hand.
            Busted. 
        '''
        self.player.set_cards([Card('A','diamond'), Card('A','heart'), Card('3','heart'), Card('7','heart'), Card('3','spade'), Card('7','spade')])
        self.assertEqual(self.player.calculate_score(), -1)
        
    #  Three Aces.       
    def test_calculate_score_three_Aces_zero_eleven_total_four_handcards_not_busted(self):
        '''
            Check score calculation when 3 Ace cards. 
            Zero Ace card treated as eleven.
            Total 4 cards at hand.
            Not busted.
        '''
        self.player.set_cards([Card('A','diamond'), Card('A','heart'), Card('A','spade'), Card('9','heart') ])
        self.assertEqual(self.player.calculate_score(), 12)
        
    def test_calculate_score_three_Aces_zero_eleven_total_six_handcards_not_busted(self):
        '''
            Check score calculation when 3 Ace cards. 
            Zero Ace card treated as eleven.
            Total 6 cards at hand.
            Not busted.
        '''
        self.player.set_cards([Card('A','diamond'), Card('A','heart'), Card('A','spade'), Card('3','heart'), Card('3','spade'), Card('3','diamond') ])
        self.assertEqual(self.player.calculate_score(), 12)
    
    def test_calculate_score_three_Aces_one_eleven_total_four_handcards_not_busted(self):
        '''
            Check score calculation when 3 Ace cards. 
            One Ace card treated as eleven.
            Total 4 cards at hand.
            Not busted.
        '''
        self.player.set_cards([Card('A','diamond'), Card('A','heart'), Card('A','spade'), Card('8','heart') ])
        self.assertEqual(self.player.calculate_score(), 21)
    
    def test_calculate_score_three_Aces_one_eleven_total_six_handcards_not_busted(self):
        '''
            Check score calculation when 3 Ace cards. 
            One Ace card treated as eleven.
            Total 6 cards at hand.
            Not busted.
        '''
        self.player.set_cards([Card('A','diamond'), Card('A','heart'), Card('A','spade'), Card('2','heart'), Card('2','spade'), Card('4','diamond') ])
        self.assertEqual(self.player.calculate_score(), 21)
    
    def test_calculate_score_three_Aces_total_five_handcards_busted(self):
        '''
            Check score calculation when 3 Ace cards. 
            Total 5 cards at hand.
            Busted.
        '''
        self.player.set_cards([Card('A','diamond'), Card('A','heart'), Card('A','spade'), Card('9','heart'), Card('10','heart') ])
        self.assertEqual(self.player.calculate_score(), -1)
        
    def test_calculate_score_three_Aces_total_six_handcards_busted(self):
        '''
            Check score calculation when 3 Ace cards. 
            Total 6 cards at hand.
            Busted.
        '''
        self.player.set_cards([Card('A','diamond'), Card('A','heart'), Card('A','spade'), Card('9','heart'), Card('9','spade'), Card('2','diamond') ])
        self.assertEqual(self.player.calculate_score(), -1)
        
    #  Four Aces.  
    def test_calculate_score_four_Aces_zero_eleven_total_six_handcards_not_busted(self):
        '''
            Check score calculation when 4 Ace cards. 
            Zero Ace card treated as eleven.
            Total 6 cards at hand.
            Not busted.
        '''
        self.player.set_cards([Card('A','diamond'), Card('A','heart'), Card('A','spade'), Card('A','club'), Card('7','club'), Card('10','club') ])
        self.assertEqual(self.player.calculate_score(), 21)
    
    def test_calculate_score_four_Aces_one_eleven_total_four_handcards_not_busted(self):
        '''
            Check score calculation when 4 Ace cards. 
            One Ace card treated as eleven.
            Total 4 cards at hand.
            Not busted.
        '''
        self.player.set_cards([Card('A','diamond'), Card('A','heart'), Card('A','spade'), Card('A','club') ])
        self.assertEqual(self.player.calculate_score(), 14)
        
    def test_calculate_score_four_Aces_one_eleven_total_six_handcards_not_busted(self):
        '''
            Check score calculation when 4 Ace cards. 
            One Ace card treated as eleven.
            Total 6 cards at hand.
            Not busted.
        '''
        self.player.set_cards([Card('A','diamond'), Card('A','heart'), Card('A','spade'), Card('A','club'), Card('3','club'), Card('4','club') ])
        self.assertEqual(self.player.calculate_score(), 21)
        
    def test_calculate_score_four_Aces_total_six_handcards_busted(self):
        '''
            Check score calculation when 4 Ace cards. 
            Total 5 cards at hand.
            Busted.
        '''
        self.player.set_cards([Card('A','diamond'), Card('A','heart'), Card('A','spade'), Card('A','club'), Card('8','club'), Card('10','club')])
        self.assertEqual(self.player.calculate_score(), -1)
        
    def test_calculate_score_one_face_cards_not_busted(self):
        '''
            Check score calculation when there are a total of one face card.
            The player is not busted.
        '''
        self.player.set_cards([Card('J','diamond')])
        self.assertEqual(self.player.calculate_score(), 10)   

    def test_calculate_score_one_face_cards_busted(self):
        '''
            Check score calculation when there are a total of one face card.
            The player is busted.
        '''
        self.player.set_cards([Card('J','diamond'),Card('10','diamond'), Card('10','diamond') ])
        self.assertEqual(self.player.calculate_score(), -1) 

    def test_calculate_score_two_face_cards_not_busted(self):
        '''
            Check score calculation when there are a total of two face cards.
            The player is not busted.
        '''
        self.player.set_cards([Card('J','diamond'), Card('K','heart')])
        self.assertEqual(self.player.calculate_score(), 20)
                
    def test_calculate_score_two_face_cards_busted(self):
        '''
            Check score calculation when there are a total of two face cards.
            The player is busted.
        '''
        self.player.set_cards([Card('J','diamond'), Card('K','heart'), Card('10','heart')])
        self.assertEqual(self.player.calculate_score(), -1)   
        
    def test_calculate_score_three_face_cards_busted(self):
        '''
            Check score calculation when there are a total of three face cards.
            The player is busted.
        '''
        self.player.set_cards([Card('J','diamond'), Card('K','heart'), Card('Q','heart')])
        self.assertEqual(self.player.calculate_score(), -1) 
    
    def test_draw_success(self):
        '''
            Check if draw() returns True when prob to draw is set to 1.
        '''
        self.player._prob_to_draw = 1
        self.assertTrue(self.player.draw())
        
    def test_draw_fail(self):
        '''
            Check if draw() returns False when prob to draw is set to 0.
        '''
        self.player._prob_to_draw = 0
        self.assertFalse(self.player.draw())
    
    def test_draw_decision_ratio(self):
        '''
            Check if draw() correctly draws according to specified probability to draw.
            It uses monte carlo simulation with tolerance level set to 0.01.
        '''
        self.player._prob_to_draw = 0.3
        for test_idx in range(5):
            num_draws = 0
            num_trials = int(1e5)
            for trial in range(num_trials):
                num_draws += self.player.draw()
            self.assertAlmostEqual(num_draws/num_trials,0.3, delta=0.01)
            
    def test_dealer_draw_decision_rate_when_score_below_17(self):
        '''
            Check if dealer always draws when score is below 17.
        '''
        self.dealer._cards = [Card('10', 'heart'), Card('6', 'heart')]
        num_draws = 0
        num_trials = int(1e5)
        for trial in range(num_trials):
            num_draws += self.dealer.draw()
        self.assertEqual(num_draws, num_trials)
    
    def test_dealer_draw_decision_rate_when_score_equal_17(self):
        '''
            Check if dealer draws according to the specified probability of drawing when score is equal 17.
        '''
        self.dealer._cards = [Card('10', 'heart'), Card('7', 'heart')]
        for test_idx in range(5):
            num_draws = 0
            num_trials = int(1e5)
            for trial in range(num_trials):
                num_draws += self.dealer.draw()
            self.assertAlmostEqual(num_draws/num_trials,0.4, delta=0.01)
    
    def test_dealer_draw_decision_rate_when_score_above_17(self):
        '''
            Check if dealer draws according to the specified probability of drawing when score is above 17.
        '''
        self.dealer._cards = [Card('10', 'heart'), Card('9', 'heart')]
        for test_idx in range(5):
            num_draws = 0
            num_trials = int(1e5)
            for trial in range(num_trials):
                num_draws += self.dealer.draw()
            self.assertAlmostEqual(num_draws/num_trials,0.4, delta=0.01)