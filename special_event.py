def special_event(round_num, player1, coins, board, roll):
    if round_num % 4 == 0:
        print (f"Special Round Triggered!!!!")
        if roll == 8:
            if coins[player1] >= 2:
                coins[player1] -= 2
                board[8] += 2 #room 7 will be at  index 8
                print(f"{player1} rolled 8: put 2 coins in room 7 please.")
            else:
                print(f"{player1} rolled 8 but doesn’t have enough coins.")
        
        if roll == 10:
            if board[8] >= 2:
                coins[player1] += 2
                board[8] -= 2
                print(f"{player1} rolled 10! They can take 2 coins from room 7")
            else:
                print(f"there's not enough coins in room 7 for you to take :("
                      f"Try again next time!")
                return True
    return False