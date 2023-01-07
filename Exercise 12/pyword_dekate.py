"""
Author: Rohan Dekate, dekate@purdue.edu
Assignment: 12.1 - Pyword
Date: 11/14/2022

Description:
    A word guessing game where the player attempts 
    to guess a secret word.
    After each guess, the program will reveal which 
    letters from the guess that are in the secret 
    word and in the correct position, which are in the 
    secret word but in the wrong position, and which are
    not in the secret word.

Contributors:
    Name, login@purdue.edu [repeat for each]

My contributor(s) helped me:
    [ ] understand the assignment expectations without
        telling me how they will approach it.
    [ ] understand different ways to think about a solution
        without helping me plan my solution.
    [ ] think through the meaning of a specific error or
        bug present in my code without looking at my code.
    Note that if you helped somebody else with their code, you
    have to list that person as a contributor.

Academic Integrity Statement:
    I have not used source code obtained from any unauthorized
    source, either modified or unmodified; nor have I provided
    another student access to my code.  The project I am
    submitting is my own original work.
"""

"""Import additional modules below this line (starting with unit 6)."""
import random

"""Write new functions below this line (starting with unit 4)."""
def main_menu():
    '''At the start of your program, the player should be presented with a main menu from which
they can choose between starting a new game, viewing the hall of fame, or exiting the program.
If the player enters an invalid choice, the program should display an appropriate error mes-
sage and let the player try again until a valid selection is made. The program should end if the
player chooses to exit.'''
    print('Welcome to PyWord.')
    print()
    print('----- Main Menu -----')
    print('1. New Game')
    print('2. See Hall of Fame')
    print('3. Quit')
    print()
    user_input = input('What would you like to do? ')
    if user_input == '3':
        print('Goodbye.')
    if user_input == '1':
        player_name = input('Enter your player name: ')
        print(f"Hello {player_name}")
        start_game()
    else:
        print()
        print('Invalid choice. Please try again.')
        print()
        main_menu()
    return user_input

def read_txt_file():
    all_words = []
    with open('words.txt') as fo:
        for line in fo:
            line = line.strip('\n')
            all_words.append(line)
    #print(len(all_words))
    return all_words
    
def pick_game_words(all_words):
    game_words = []
    while len(game_words)<3:
        w = random.choice(all_words)
        if w not in game_words:
            game_words.append(w.lower())
    print(game_words)
    return game_words

def start_game():
    round = 1
    while round <=3:
        print()
        print(f"Round {round}:")
        turn = 1
        while turn <=6:
            guess = input(f"{turn}? ")
            if len(guess)!=5:
                print('Invalid guess. Please enter exactly 5 characters.')
            elif guess.isalpha() == False:
                print('Invalid guess. Please only enter letters.')
            else:
                pass
                turn = turn+1
        round = round +1
    pass
# Define a main function
def main():
    """Write your mainline logic below this line (then delete this line)."""
    all_words = read_txt_file()
    three_words = pick_game_words(all_words)
    call_menu = main_menu()
    start_game(three_words)
    
    
"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
