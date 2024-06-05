from src.player import Player, Dealer
from src.card import Card
from src.deck import Deck
import random

class Game:
    def __init__(self, dealer_info: tuple[str, float] = None, players_info: list[tuple[str, float]] = None):
        '''
            players: a list of players for the game.
            Constructing a card pool which is a list of Card objects with 1-9, J,Q,K,A. Each 4 cards. No jokers.
            Construct a field for turning number which indicates the current turn number of the game.
            Construct a field for the list of players in the game.
        '''
        self._turn_number = 0
        self._deck = Deck()
        if not dealer_info:
            self._dealer = None
        else:
            self._dealer = Dealer(dealer_info[0], dealer_info[1]) 
        if not players_info:
            self._players = None
        elif (len(players_info) > 25):
            raise ValueError('Max number of players is 25.')
        else:
            self._players = [Player(player_id, prob_to_draw) for player_id, prob_to_draw in players_info]
                
    def __str__(self) -> str:
        '''
            toString method.
        '''
        return (f"Game object with number of players: {self.get_num_players()}, "
                f"current turn number: {self._turn_number}, "
                f"available card pool: {[ str(card) for card in self._deck._cards]}, "
                f"dealer: {str(self._dealer)}"
                f"players: {[str(player) for player in self._players]}")
    
    def print_essential_info(self) -> str:
        return (f'Game with {self.get_num_players()} players, current turn number is {self._turn_number}')
        
    def get_turn_number(self):
        return self._turn_number
        
    def get_players(self) -> list[Player]:
        return self._players
    
    def get_num_players(self) -> int:
        '''
            Return number of players in the game.
        '''
        return len(self._players)
    
    def add_player(self, player: Player) -> bool:
        '''
            Add a player to the end of player list.
            Return True if successful.
        '''
        if len(self._players) == 25:
            raise Exception('Max number of players is 25.')
        self._players.append(player)
        return True
    
    def remove_player(self, player_id: str) -> bool:
        '''
            Remove a player from list of players specified by the player id.
            Return True if successful.
        '''
        if not isinstance(player_id, str):
            raise TypeError('Player id number be of type string.')
        for player, idx in enumerate(self._players):
            if player._player_id == player_id:
                self._players.pop(idx)
                return True
        return False
    
    def is_game_end(self) -> bool:
        '''
            Return True if all players have had their turns.
            Return False otherwise.
        '''
        if len(self._players) == 0:
            return True
        return self._turn_number == len(self._players)
    
    def assign_initial_two_cards(self) -> bool:
        '''
            Assign initial two cards to dealer and each player.
            Return True if successful.
        '''
        if self._deck.get_num_remaining_cards() < (len(self._players)+1)*2:
            raise Exception('Deck is empty.')
        self._deck.issue_card(player = self._dealer, num_cards_to_issue = 2)
        for player in self._players:
            self._deck.issue_card(player = player, num_cards_to_issue = 2)
        return True
        
    def run_dealer_turn(self) -> bool:
        '''
            Dealer's turn to draw card.
            Return True if successfully draws card.
        '''
        while self._dealer.is_alive() and self._deck.get_num_remaining_cards() > 0 and self._dealer.draw():
            self._deck.issue_card(self._dealer)
        return True
                
    def run_player_turn(self) -> bool:
        '''
            The next player in the turn draws cards.
            Return True if successful.
            Return False if no next player.
        '''
        if self.turn_number >= len(self._players):
            raise Exception('Everyone had their turns. No more turns.')
        player = self._players[self._turn_number]
        while player.is_alive() and self._deck.get_num_remaining_cards() > 0 and player.draw():
            self._deck.issue_card(player)
        self._turn_number += 1
        return True
        
    def get_blackjacks(self) -> list[Player]:
        '''
            Return the list of dealer and players whose initial two cards sum to 21.
        '''
        blackjack_players = []
        if self._dealer.is_blackjack():
                blackjack_players.append(self._dealer)
        for player in self._players:
            if player.is_blackjack():
                blackjack_players.append(player)
        return blackjack_players
    
    def get_winners(self) -> list[Player]:
        '''
            Return the list of dealer and players with equal highest score at the end of the game.
        '''
        winners = []
        if self._dealer.is_alive():
            winners.append(self._dealer)
        for player in self.players:
            if player.is_alive():
                if not winners:
                    winners.append(player)
                elif player.score > winners[0]:
                    winners = []
                    winners.append(player)
                elif player.score == winners[0]:
                    winners.append(player)
        return winners
    
    def reset_game(self, dealer_info: tuple[str, float] = None, players_info: list[tuple[str, float]] = None) -> bool:
        '''
            Reset the game.
            Reset card pool, turn number and optionally resetting the list of players if given. 
            Return True if successful.
        '''
        self._turn_number = 0
        if not dealer_info:
            self._dealer = None
        else:
            self._dealer = Dealer(dealer_info[0], dealer_info[1]) 
        if not players_info:
            self._playerss = None
        else:
            self._players = [Player(player_id, prob_to_draw) for player_id, prob_to_draw in players_info]
        return True
        