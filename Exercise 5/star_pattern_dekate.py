"""
Author: Rohan Dekate, dekate@purdue.edu
Assignment: 05.3 - Star Pattern
Date: 09/29/2022

Description:
    Draw a star pattern that has 
    a user specified number of points.

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
from operator import length_hint
from turtle import *

"""Write new functions below this line (starting with unit 4)."""


def start():
    """This function initializes the window and the turtle.
    Do not modify this function or any of the properties it sets.
    """
    setup(564, 564)
    width(7)
    side_length = 60 # Also the radius of a circle enclosed by the star.
    penup()
    goto(0, -side_length) # Start at the bottom of the star.
    pendown()

def main():
    """Write your mainline logic below this line (then delete this line)."""
    points = int(input('How many points on the star? '))
    length = 60
    inner_angle = 360/points #A
    outer_angle = 2*inner_angle #B
    color('black', '#cfb991')
    begin_fill()
    # set heading
    right((180 - outer_angle)/2)
    # Draw the star pattern
    for l in range(0,points):   
        forward(length) # Move forward
        left(180-inner_angle) # Take left
        forward(length) # Move forward
        right(180-outer_angle) # Take right
        #repeat
    end_fill()

"""Do not change anything below this line."""
if __name__ == '__main__':
    start()
    main()
    done()
