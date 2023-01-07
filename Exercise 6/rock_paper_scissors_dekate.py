"""
Author: Rohan Dekate, dekate@purdue.edu
Assignment: 06.2 - Rock Paper Scissors
Date: 10/03/2022

Description:
    Rock-Paper-Scissors game with computer.
    3 separate functions for generating computer choice, 
    validating user entry and evaluating the winner.

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
import random as r # Import random module as alias r

"""Write new functions below this line (starting with unit 4)."""
# Get computer choice
def get_computer_choice():
    options = ['rock','paper','scissors']
    comp_choice = r.choice(options)
    return comp_choice
# Check player's entry for validity of string
def get_player_choice():
    user_choice = input('Choose rock, paper, or scissors: ')
    while (user_choice != 'rock' and user_choice != 'paper' and user_choice != 'scissors'):
        print('You made an invalid choice. Please try again.')
        user_choice = input('Choose rock, paper, or scissors: ')
    return user_choice
# Evaluate the winner
def get_winner(computer,player):
    if computer == player:
        win = 'tie'
    elif computer == 'rock' and player == 'scissors':
        win = 'computer'
    elif computer == 'scissors' and player == 'paper':
        win = 'computer'
    elif computer == 'paper' and player == 'rock':
        win = 'computer'
    else:
        win = 'player'
    return win

# Define a main function
def main():
    """Write your mainline logic below this line (then delete this line)."""
    # Call computer choice function
    computer_choice = get_computer_choice()
    # Call player choice function to check validity of string
    player_choice = get_player_choice()
    # Display the choices
    print(f'  The computer chose {computer_choice}, and you chose {player_choice}.')
    # Evaluate the winner by calling function
    winner = get_winner(computer_choice,player_choice)
    if winner == 'computer':
        print(f'  {computer_choice} beats {player_choice}')
        print('  You lost.  Better luck next time.')
        print('Thanks for playing.')
    elif winner == 'player':
        print(f'  {player_choice} beats {computer_choice}')
        print('  You won the game!')
        print('Thanks for playing.')
    elif winner == 'tie':
        print("  It's a tie. Starting over.")
        print()
        main()

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
