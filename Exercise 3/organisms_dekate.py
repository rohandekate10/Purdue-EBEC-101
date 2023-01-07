"""
Author: Rohan Dekate, dekate@purdue.edu
Assignment: 03.4 - Organisms
Date: 09/12/2022

Description:
    A program that predicts the approximate size of a population of organisms.

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


"""Write new functions below this line (starting with unit 4)."""

# Define a main function
from re import I

def main():
    """Write your mainline logic below this line (then delete this line)."""
    # Ask for user input
    start = float(input('Starting population, in thousands: '))
    rate = int(input('Average daily increase, in percent: '))
    days = int(input('Number of days to multiply: '))
    # Calculate population multiplier
    multiplier = 1+(rate/100)
    print('Day'+'   '+'Approx. Pop')
    # For loop
    for d in range(0,days+1):
        if d==0:
            print(f'{d:>3}'+'   '+f'{start:>11,.3f}')
        else:
            pop = start*multiplier
            print(f'{d:>3}'+'   '+f'{pop:>11,.3f}')
            start = pop
"""Do not change anything below this line."""
if __name__ == "__main__":
    main()