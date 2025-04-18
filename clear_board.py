def clear_board(board_state, jackpot, keep_field=None):
    """
    Clears all coins from the board except optionally one room (7).
    
    args:
        board_state (dict): maps room numbers to {player: coin count}
        jackpot (int): the current jackpot value
        keep_field (int | None): a room number to exclude from clearing

    Returns:
        tuple: (total number of coins removed, updated jackpot value)
    """
    total_collected = 0
    
    for room, players in board_state.items():
        if room == keep_field:
            continue
        for player in list(players):
            total_collected += players[player]
            del players[player]
            
    if keep_field != 7:
        total_collected += jackpot
        jackpot = 0
    return total_collected, jackpot