"""
Author: Rohan Dekate, dekate@purdue.edu
Assignment: 02.4 - Time Calculator
Date: 09/19/2022

Description:
    Ask the user to enter a number of seconds and then displays 
    the total time entered in days, hours, minutes and seconds.

Contributors:
    Thirawat Bureetes, tbureete@purdue.edu [repeat for each]

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
from time import time


def main():
    """Write your mainline logic below this line (then delete this line)."""
    # Ask for user input
    time = int(input('Please enter a time in seconds: '))
    day = time//86400 # Calculate days
    td_s = time-day*24*60*60 # Calculate seconds remaining
    hours = td_s%86400//3600 # Calculate hours
    th_s = td_s-hours*60*60 # Calculate seconds remaining
    minutes = th_s%3600//60 # Calculate minutes
    tm_s = th_s-minutes*60 # Calculate seconds remaining
    # Write conditionals and display output
    if time<60:
        print(f'  {time} seconds is less than one minute.')
    else:
        print(f'  {time:,} seconds equals ', end='')
        if day:
            print(f'{day} day(s)', end='')
        if hours:
            if day:
                if minutes or tm_s:
                    print(', ', end='')
                else:
                    print(' and ', end='')
            print(f'{hours} hour(s)', end='')
        if minutes:
            if day or hours:
                if tm_s:
                    print(', ', end='')
                else:
                    print(' and ', end='')
            print(f'{minutes} minute(s)',end='')
        if tm_s:
            print(f' and {tm_s} second(s)',end='')
        print('.')

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()