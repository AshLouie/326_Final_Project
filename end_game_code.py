def end_game_check (players, special_spots):
    """Basic end game condition check code. Will end game and declare winner
        based on which condition is satisfied    

    Args:
        players (list): list of player objects
        special_spots (dict): dictionary containing special spots on board
            and how many coins they have

    Returns:
        bool: Returns True if condition is met, returns False otherwise to 
            continue game play
    """
    active_players = []
    total_player_coins = 0
    total_board_coins = 0
    
    for player in players:
        player_coins += player.coins
        if player.coins > 0:
            active_players.append(player)
            
    for coins in special_spots:
        total_board_coins += special_spots    
    total_coins = total_player_coins + total_board_coins
    
    if len(active_players) == 1:
        print (f"GAME OVER! {active_players[0]} has won the game!")
        return True
    
    for player in players:
        if player["coins"] == total_coins:
            print(f"GAME OVER! {player["name"]} wins!")
            return True
        
    return False
