"""
Author: Rohan Dekate, dekate@purdue.edu
Assignment: 05.4 - Mississippi Turtles
Date: 10/13/2022

Description:
    Write the words 'Mississippi Turtles'
    using Turtle commands

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

"""Write new functions below this line (starting with unit 4)."""


def start():
    """This function initializes the window and the turtle.
    Do not modify this function or any of the properties it sets.
    """
    setup(600, 400)
    width(9)
    color("purple")


def draw_e():
    """Write this function."""
    penup()
    forward(60)
    left(90)
    forward(30)
    pendown()
    circle(radius=30, extent=180)
    left(90)
    forward(60)
    penup()
    backward(60)
    right(90)
    pendown()
    circle(radius=30, extent=150)
    penup()
    circle(radius=30, extent=30)
    backward(30)
    right(90)
    forward(30)

def draw_i():
    """Write this function."""
    penup()
    #forward(30)
    left(90)
    pendown()
    forward(30)
    penup()
    forward(20)
    pendown()
    dot(size = 9)
    penup()
    backward(50)
    right(90)
    forward(30)

def draw_l():
    """Write this function."""
    penup()
    #forward(30)
    left(90)
    pendown()
    forward(60)
    penup()
    backward(60)
    right(90)
    forward(20)

def draw_M():
    """Write this function."""
    penup()
    forward(60)
    left(90)
    pendown()
    forward(45)
    #left(90)
    circle(radius=15, extent=180)
    forward(45)
    penup()
    backward(45)
    right(180)
    pendown()
    circle(radius=15, extent=180)
    #right(90)
    forward(45)
    penup()
    left(90)
    forward(80)

def draw_p():
    """Write this function."""
    penup()
    forward(20)
    pendown()
    circle(20)
    penup()
    backward(20)
    left(90)
    forward(50)
    pendown()
    backward(80)
    penup()
    forward(30)
    right(90)
    forward(60)

def draw_r():
    """Write this function."""
    penup()
    forward(50)
    left(90)
    forward(40)
    circle(30,90)
    pendown()
    circle(30,90)
    backward(30)
    forward(70)
    penup()
    left(90)
    forward(40)

def draw_s():
    """Write this function."""
    forward(30)
    circle(10,180)
    forward(30)
    penup()
    right(90)
    forward(20)
    #right(90)
    #forward(10)
    left(90)
    pendown()
    circle(10,180)
    penup()
    left(90)
    forward(20)
    right(90)
    pendown()
    forward(30)
    penup()
    right(90)
    forward(40)
    left(90)
    forward(30)

def draw_t():
    """Write this function."""
    penup()
    forward(30)
    left(90)
    pendown()
    forward(60)
    penup()
    backward(20)
    right(90)
    forward(20)
    pendown()
    backward(40)
    penup()
    forward(20)
    right(90)
    forward(40)
    left(90)
    forward(40)

def draw_u():
    """Write this function."""
    penup()
    left(90)
    forward(60)
    pendown()
    backward(30)
    right(180)
    circle(30,180)
    forward(30)
    backward(60)
    penup()
    right(90)
    forward(40)

def main():
    """After these lines, call your letter drawing functions
    as needed to draw the words "Mississippi turtles".
    """
    #speed=1
    penup()
    goto(-280,100)
    pendown()

    draw_M()
    draw_i()
    pendown()
    draw_s()
    pendown()
    draw_s()
    draw_i()
    pendown()
    draw_s()
    pendown()
    draw_s()
    draw_i()
    draw_p()
    draw_p()
    draw_i()
    
    penup()
    goto(-200,-100)
    pendown()
    draw_t()
    draw_u()
    draw_r()
    draw_t()
    draw_l()
    draw_e()
    pendown()
    draw_s()
    

"""Do not change anything below this line."""
if __name__ == '__main__':
    start()
    main()
    done()
