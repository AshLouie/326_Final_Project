"""Final code we will be using for our in-class presentation of our program
"""

import random
import argparse

def clear_board(board, skip_room=None):
    """
    Clears coins from all rooms on the board except one optional room.

    Args:
        board (dict): Dictionary mapping room numbers to coin counts.
        skip_room (int or None): Room number to exclude from clearing.

    Returns:
        int: Total number of coins removed from the board.
    """
    total = 0
    for room in board:
        if room == skip_room:
            continue
        total += board[room]
        board[room] = 0
    return total


def turn(player, board): 
    """what goes on a single normal turn

    Args:
        player (list): coins in your bank
        board (list): coins on the board

    Returns:
        str: messages of what you rolled and what changes to player and board
    """
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    total = die1 + die2
    message = f"You rolled a {total}. "

    if total == 2: # Lucky Pig
        earnings = clear_board(board, skip_room=7)
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
        earnings = clear_board(board)
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
        
        
if __name__ == "__main__":
    """
    Parses input arguments, initializes game state, and runs the game loop.

    Runs until only one player has coins remaining.
    """
    parser = argparse.ArgumentParser(description= "Single turn of Gluckshaus")
    parser.add_argument("names", nargs="+", help="Names of players")
    parser.add_argument("coins", type = int, help= "Starting number of coins")
    args = parser.parse_args()
    
    players = [{'name': name, 'coins': args.coins} for name in args.names]
    board = {room: 0 for room in [3, 5, 6, 7, 8, 9, 10, 11]}
    
    round_num = 1
    game_over = False

    while not game_over:
        print(f"\n=== Round {round_num} ===")
        
        for player in players:
            if player["coins"] == 0:
                print(f"{player['name']} has no coins. Skipping turn.")
                continue

            print(f"\n{player['name']}'s turn:")
            result = turn(player, board)
            print(result)
            print(f"{player['name']} now has {player['coins']} coins.")

        print("\n-- Board --")
        for room in sorted(board):
            print(f"Room {room}: {board[room]} coin(s)")

        active_players = [p for p in players if p["coins"] > 0]
        if len(active_players) == 1:
            print(f"\nGAME OVER! {active_players[0]['name']} wins!")
            game_over = True
        elif len(active_players) == 0:
            print("\nGAME OVER! No coins left. Tie!")
            game_over = True    
        else:
            input("\nPress Enter to continue to the next round...")
            round_num += 1