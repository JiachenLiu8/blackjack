from src.card import Card
import random

class Player:
    def __init__(self,player_id: str, prob_to_draw: float):
        '''
            player_number: the player number for the player.
            Construct player number.
            Construct self._cards which is a dict of Card objects that player has at hand
            # self._cards: {str, int}. Key is content of card and value is the number of such cards. 
            self._card: list of Card object.
        '''
        self._player_id = player_id
        self._cards = []
        self._score = 0
        if not isinstance(prob_to_draw, float) and not isinstance(prob_to_draw, int):
            raise TypeError('probability of drawing should be type float')
        if prob_to_draw < 0 or prob_to_draw > 1:
            raise ValueError('probability of drawing card must be between 0 and 1')
        self._prob_to_draw = float(prob_to_draw)
        
    def __eq__(self, other) -> bool:
        return (self._player_id == other._player_id and 
                self._prob_to_draw == other._prob_to_draw and 
                self._cards == other._cards and 
                self._score == other._score)

    def set_cards(self, cards: list[Card]) -> bool:
        for card in cards:
            if not isinstance(card, Card):
                raise TypeError('input needs to be a list of Card objects')
        self._cards = cards
        return True
    
    def add_card(self, card: Card) -> bool:
        if not isinstance(card, Card):
            raise TypeError('input card must be Card object')
        self._cards.append(card)
        return True

    def get_cards(self) -> list[Card]:
        '''
            Getter for self._cards.
        '''
        return self._cards
    
    def set_player_id(self, player_id: str) -> bool:
        if not isinstance(player_id, str):
            raise TypeError('player_id must be int')
        if len(player_id) == 0:
            raise ValueError('player_id can not be empty string')
        self.player_id = player_id
        
    def get_player_id(self) -> str:
        return self._player_id
    
    def set_prob_to_draw(self, prob_to_draw: float) -> bool:
        if not isinstance(prob_to_draw, float) and not isinstance(prob_to_draw, int):
            raise TypeError('probability of drawing should be type float')
        if prob_to_draw < 0 or prob_to_draw > 1:
            raise ValueError('probability of drawing card must be between 0 and 1')
        self._prob_to_draw = float(prob_to_draw)
        return True
    
    def get_prob_to_draw(self) -> float:
        return self._prob_to_draw
        
    def calculate_score(self):
        '''
            Calculate the total score of cards.
            Return the total score if the score is <= 21.
            Return -1 if total score if > 21.
        '''
        if len(self._cards) == 0:
            return 0
        score = 0
        num_aces = 0
        for card in self._cards:
            if card.is_ace():
                num_aces += 1
            else:
                score += card.score()
        score += num_aces
        if score > 21:
            self._score = -1
            return -1
        else:
            score += min((21 - score) // 10, num_aces) * 10 
            self._score = score
            return score
    
    def is_blackjack(self) -> bool:
        ''' 
            Check if the initial two cards adds up to 21.
            Return True if the score of cards at hand when the game beginns equals 21.
        '''
        return len(self._cards) == 2 and self.calculate_score() == 21
    
    def draw(self) -> bool:
        '''
            Randomly deciding whether to drawaccording to the probability of drawing of the player.
            Returns a boolean indicating the drawing decision.
        '''
        return random.uniform(0, 1) < self._prob_to_draw
    
    def action(self) -> str:
        '''
            Return a string indicating drawing action.
        ''' 
        if random.uniform(0, 1) < self._prob_to_draw:
            return 'Decide to draw.'
        else:
            return 'Decide not to draw.'
    
    def is_alive(self) -> bool:
        '''
            Check if the player is still possible to be a winner.
            Return True if the score of cards is <=21. 
            Return False otherwise.
        '''
        return self.calculate_score() != -1
    
    def __str__(self) -> str:
        '''
            For printing the object.
        '''
        return (f"Player object with player_id: {self._player_id}, "
                f"current score: {self._score}, "
                f"probability of drawing card: {self._prob_to_draw}, "
                f"cards at hand: {[str(card) for card in self._cards]}")
        # use parentheses for line continuation
        # For f-string, you can just split the string into multiple f-strings enclosed in parentheses. Python will automatically concatenate them
    
class Dealer(Player):
    def draw(self) -> bool:
        '''
            If score < 17, draw a card. 
            Otherwise, randomly deciding whether to drawaccording to the probability of drawing of the player.
            Returns a boolean indicating the drawing decision.
        '''
        if self.calculate_score() < 17:
            return True
        else:
            return random.uniform(0, 1) < self._prob_to_draw
        
    def action(self) -> str:
        '''
            Return a string indicating drawing action.
        ''' 
        if self.calculate_score() >= 17 and random.uniform(0, 1) < self._prob_to_draw:
            return 'Decide to draw.'
        else:
            return 'Decide not to draw.'