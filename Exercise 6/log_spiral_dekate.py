"""
Author: Rohan Dekate, dekate@purdue.edu
Assignment: 06.4 - Log Spiral
Date: 10/06/2022

Description:
    Draw logarithmic spiral using turtle commands.

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
from turtle import *
import math


"""Write new functions below this line (starting with unit 4)."""


def start():
    """This function initializes the window and the turtle.
    Do not modify this function or any of the properties it sets.
    """
    setup(564, 564)
    width(5)


def main():
    """Write your mainline logic below this line (then delete this line)."""
    a = 4
    b = 0.22
    #setpos(0,0)
    penup()
    for i in range(0, 1081):
      # Draw a spiral
        theta = math.radians(i) # Set angle
        x = a*math.exp(b*theta)*math.cos(theta) # x coordinate
        y = a*math.exp(b*theta)*math.sin(theta) # y coordinate
        setpos(x, y) # draw the spiral as per x and y
        pendown()


"""Do not change anything below this line."""
if __name__ == "__main__":
    start()
    main()
    done()
