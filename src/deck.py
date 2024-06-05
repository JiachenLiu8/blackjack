from src.card import Card
from src.player import Player
import random

class Deck:
    def __init__(self):
        self._cards = []
        for face_value in range(2, 11):
            for suit in ['club','diamond','heart','spade']:
                self._cards.append(Card(str(face_value), suit))
        for face_value in ['J','Q','K','A']:
            for suit in ['club','diamond','heart','spade']:
                self._cards.append(Card(face_value, suit))
        self._idx_of_next_card_to_issue = 0
                
    def __str__(self) -> str:
        return f'Deck with cards: {[str(card) for card in self._cards]}'
    
    def __eq__(self, other) -> bool:
        return self._cards == other._cards
    
    def set_cards(self, cards: list[Card]) -> bool:
        if not all(isinstance(card, Card) for card in cards):
            raise TypeError('Input cards must be a list of Card objects')
        self._cards = cards
            
    def get_cards(self) -> list[Card]:
        return self._cards
    
    def _swap_card(self,i: int, j: int):
        '''
            Swap cards on idx i and index j.
        '''
        if i == j:
            return 
        temp = self._cards[i]
        self._cards[i] = self._cards[j]
        self._cards[j] = temp
    
    def shuffle_cards(self) -> bool:
        if not self._cards:
            raise Exception('Can not shuffle empty deck of cards.')
        for i in range(len(self._cards)):
            idx = random.randint(i, len(self._cards)-1)
            self._swap_card(i, idx)
        return True
    
    def issue_card(self, player: Player, num_cards_to_issue: int = 1) -> bool:
        '''
            player: player or dealer.
            num_cards_to_issue: number of cards to issue.
            Randomly draws a card from the remaining card pool of the game.
            Append this card to players cards at hand.
            Return True if sucessful.
            Raise Exception if no more cards available in the card pool.
        '''
        for i in range(num_cards_to_issue):
            if self.get_num_remaining_cards() == 0:
                raise Exception('Deck is already empty.')
            player._cards.append(self._cards[self._idx_of_next_card_to_issue]) # use player._cards to directly access field. No need to use getter/setter inside.
            self._idx_of_next_card_to_issue += 1
        return True
       
    def get_num_remaining_cards(self) -> int:
        '''
            Return the number of remaining available cards that have not been issued.
        '''
        return len(self._cards) - self._idx_of_next_card_to_issue
   
  # def add_card(self, card_to_add: Card) -> bool:
    #     '''
    #         Add the card if there is not a card with same suit and face_value in the deck.
    #         Return True if successfully add.
    #         Return False otherweise.
    #     '''
    #     for card in self._cards:
    #         if card == card_to_add:
    #             raise Exception('One deck of cards can no have two cards with same suit and face_value.')     
    #     self._cards.append(card)
    #     return True
        
    # def remove_card(self, target_card: Card) -> bool:
    #     for card, idx in enumerate(self._cards):
    #         if card == target_card:
    #             self._cards.pop(idx)
    #             return True
    #     raise Exception('Removing from empty deck of cards.')