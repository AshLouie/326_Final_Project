# 326_Final_Project
Final Project for INST326.

# Running Our Program
To run our program in the terminal, you should follow these few steps:
    1. Navigate to the folder in which our program lives

    2. First, input "python final_program.py"

    3. Then, enter the names of the players. There must be at least two names
    for the program to run properly

    4. You will then enter the number of coins you want each player to start
    with.

    5. An example terminal input looks like this:

        a. 'python final_program.py Ash Chappon Nhi Justin 10'

    6. The program will give you clear instructions on how to move through each
    round, and will give a clear end game message if the conditions are met.

# Files in Repo

## collaborative_programming.py
File used to show teams ability to use Git.

## in_class_presentation_code.py
File used to combine code for the sake of the in-class presentation. Basic game 
play to illustrate vision of game.

## clear_board.py
First iteration of function that would reset the board after/before each round
played. Will remove all coins from rooms except for one room, room 7.

## turn.py
Function that takes a number rolled by randint and takes or removes coins 
from the board depending on the amount. The specific conditions are: 
    - On a roll of 3, 5, 6, 8, 9, 10 or 11, the player places a coin on the 
    board if that room is empty, or takes the coin if it is occupied.

    - If the player rolls snake eyes(1 on both dice), he has rolled a 
    "Lucky Pig" and collects all the coins on the board, except for what 
    lies in room 7.

    - If the player rolls a 12, he is "king" and wins all coins on the board.

    - If the player rolls a 7, there is a "wedding" going on in the room, and 
    one has to put a coin on there no matter what. This builds up a jackpot 
    until the "king" (12) is rolled.

    - If the player rolls a 4, nothing happens and they get to skip a turn.

## special_event.py
Every 4 rounds, this function will add a trigger event where the rule changes up
from the regular rule of the game. Any player that rolls an 8, they will have 
to put 2 coins in room 7 (instead of 1 coin in room 8), and if the player rolls
a 10, they can take 2 coins in room 7. However, the algorithm will need the 
current state of the game to see where the coins are on the board and if there
are no coins in room 7 for the player that rolls a 10, then they would get to
skip their turn. The rule would stay the same for all other numbers.

## end_game_code.py
First iteration of the function that will check each round, whether or not a 
certain set of criteria are met, initiating the end game sequence. This function 
will check these criteria:

    - Whether or not spaces have coins

    - One player has acquired all of the coins

If all of these criteria are met, the end game sequence will begin.

## final_program.py
The final draft of our program. This file contains all of our individual 
functions with any necessary changes made to allow program to run from the 
terminal and meet all assignment criteria. 

## valid_name.py
The function that check if the player's name is valid. A player's name can only
contains letters.

# Annotated Bibliography
Baron Aurddeilen-ap-Robet. (2017, March 11). Gambling Games. Medieval People at 
    Play. https://rusticadornments.wordpress.com/2017/03/11/gambling-games/

Ivan Beldiagin. (2019, June 3). Glückshaus Is a Simple Medieval Gambling Dice 
    Game. Instructables; Instructables. 
    https://www.instructables.com/Gl%C3%BCckshaus-House-of-Fortune-Is-a-Medieval-Gambling/

Wikipedia Contributors. (2024, May 29). Glückshaus. Wikipedia; Wikimedia 
    Foundation. https://en.wikipedia.org/wiki/Gl%C3%BCckshaus

# Attribution Table
|*Method/function*|*Primary Author*|*Techniques Demonstrated*|
|-----------------|----------------|-------------------------|
|def end_game_check|Ashleigh Louie |f-strings containing     |
|def end_game_check|Ashleigh Louie|comprehensions or generator expressions|
|def turn|Justin Namgung|randomization|
|def turn|Justin Namgung|if-else statements|
|def clear_board|Chapponarot Bornhor|iteration over a dictionary|
|__main__ game loop|Chapponarot Bornhor|argument parsing|
|parse_args| Nhi Vu|ArgumentParser class
|def valid_name|Nhi Vu| regular expressions
