"""Final code we will be using for our in-class presentation of our program
"""

import random
import argparse
import re 

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
        
        
def special_event(round_num, player, board):
    """
    Triggers a special event every 4th round of the game.

    Args:
        round_num (int): the current round number
        player (dict): the dictionary contain "name" and "coin"
        board (dict): the board mapping out room numbers to coin counts.

    Returns:
        bool: True if a special event occurred, False otherwise
    """
    if round_num % 4 == 0:
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        total = die1 + die2
        print (f"Special Round Triggered!!!!")

        if total == 8:
            if player["coins"] >= 2:
                player["coins"] -= 2
                board[7] += 2 
                print(f"{player["name"]} rolled 8: put 2 coins in room 7 please.")
            else:
                print(f"{player["name"]} rolled 8 but doesn’t have enough coins.")
        
        if total == 10:
            if board[8] >= 2:
                player["coins"] += 2
                board[8] -= 2
                print(f"{player["name"]} rolled 10! They can take 2 coins from room 7")
            else:
                print(f"there's not enough coins in room 7 for you to take :("
                      f"Try again next time!")
                return True
    return False


def valid_name(name):
    """
    Check if the input's name is valid

    Args:
        name (str): player's name
    """
    pattern = r"[a-zA-Z]*$"
    return re.match(pattern, name) is not None


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
    
    active_players = [player for player in players if player.coins > 0]
            
    for coins in special_spots.values():
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
        
if __name__ == "__main__":
    """
    Parses input arguments, initializes game state, and runs the game loop.

    Runs until only one player has coins remaining.
    """
    parser = argparse.ArgumentParser(description= "Single turn of Gluckshaus")
    parser.add_argument("names", nargs="+", help="Names of players")
    parser.add_argument("coins", type = int, help= "Starting number of coins")
    args = parser.parse_args()
    
    valid_names = []

    for name in args.names:
        if valid_name(name):
            valid_names.append(name) 
        else:
            print(f"Invalid name '{name}'. Must contains only letters.")
            name = input("Please enter a valid name: ")
    
    players = [{'name': name, 'coins': args.coins} for name in valid_names]
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

            special_event(round_num, player, board)
            
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