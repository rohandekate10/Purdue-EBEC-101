"""
Author: Rohan Dekate, dekate@purdue.edu
Assignment: 06.3 - Random Vowels
Date: 10/06/2022

Description:
    Draw vowels in random order by importing a .py file.

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

"""Import modules below this line (starting with unit 6)."""
from turtle import *
# Import vowels.py file
import vowels
# Import random module for shuffling
import random as r


"""Write new functions below this line (starting with unit 4)."""


def start():
    """This function initializes the window and the turtle.
    Do not modify this function or any of the properties it sets.
    """
    setup(600, 400)
    width(9)
    speed(0)
    penup()
    goto(-220, -30)


def main():
    """Write your mainline logic below this line (then delete this line)."""
    # Set posiiton of turtle
    penup()
    setpos(-150,0)
    pendown()
    # Initialize a list of vowels
    vow = ['a','e','i','o','u']
    # Shuffle the list in place to generate a random order
    r.shuffle(vow)
    #print(vow)
    # Draw the vowels as per the shuffled order in the list
    # Call the functions from vowels.py file
    for v in vow:
        if v == 'a':
            vowels.draw_a()
        elif v == 'e':
            vowels.draw_e()
        elif v == 'i':
            vowels.draw_i()
        elif v == 'o':
            vowels.draw_o()
        elif v == 'u':
            vowels.draw_u()

"""Do not change anything below this line."""
if __name__ == "__main__":
    start()
    main()
    done()
