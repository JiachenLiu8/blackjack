from src.game import Game 

# main 算外部了，所以必须用getter和setter，不能直接用dot method来access field。
# main 就是在外部调用API，API给你啥功能你用啥，里面不对你开放。
# main 一般不return 任何东西。（就是return None）
def main():
    dealer_info = ('dealer_id', 0.3)
    players_info = [('player1',0.3), ('player2', 0.4), ('player3', 0.5)]
    game = Game(dealer_info, players_info)
    game.assign_initial_two_cards()
    blackjack_players = game.get_blackjacks()
    if blackjack_players:
        print(f'blackjack players are: {[player.get_player_id() for player in blackjack_players]}')
        return 
    game.run_dealer_turn()
    while not game.is_game_end():
        game.run_player_turn()
    winners = game.get_winners()
    if winners:
        print(f'winners are: {[winner.get_player_id() for winner in winners]}')
    else:
        print('no winners.')

       