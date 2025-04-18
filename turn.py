import random

def turn(player, board): 
    # player = you, the player
    # board = the game board
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    total = die1 + die2
    message = f"You rolled a {total}."

    if total == 2: # Lucky Pig
        earnings = sum(coins for room, coins in board.items() if room != 7)
        for room in board:
            if room != 7:
                board[room] = 0
        player['coins'] += earnings
        return message + f"Lucky Pig! \
            Collect {earnings} coins from the entire board minus room 7."
    
    if total == 4: # Unlucky Pig
        return message + f"Unlucky Pig! Skip Turn."
    
    if total == 7: # Wedding
        if player['coins'] > 0:
            player['coins'] -= 1
            board[7] += 1
            return message + f"Wedding! Place 1 coin in room 7."
        else:
            return message + f"Wedding! No coins to place."
    
    if total == 12: # King
        earnings = sum(board.values())
        for room in board:
            board[room] = 0
        player['coins'] += earnings
        return message + f"King! Collect all {earnings} coins from the board."
    
    if total in board: # Other; Rooms 3, 5, 6, 8, 9, 10, 11
        if board[total] == 0:
            if player['coins'] > 0:
                player['coins'] -= 1
                board[total] += 1
                return message + f"Room {total} was empty. Place 1 coin."
            else:
                return message + f"Room {total} was empty. No coins to place."
        else:
            player['coins'] += 1
            board[total] -= 1
            return message + f"Room {total} was occupied. Take 1 coin."
            
