"""
Author: Rohan Dekate, dekate@purdue.edu
Assignment: 03.3 - Rainfall
Date: 09/12/2022

Description:
    Collect data and calculate the total and average rainfall 
    over a period of years.

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
from timeit import repeat

def main():
    """Write your mainline logic below this line (then delete this line)."""
    year = int(input('Enter the number of years: ')) #  ask for the number of year
    month = year*12
    total = 0
    calendar_months = ['Jan.','Feb.','Mar.','Apr.','May.','Jun.','Jul.','Aug.','Sep.','Oct.','Nov.','Dec.'] # list of months
    if year<=0: # condition to check invalid year
        print('Invalid input; years must be greater than 0.')
    else: # loop for calculating total
        for y in range(1,year+1):
            print(f'  For year No. {y}')
            rainfall = 0
            for m in calendar_months:
                rainfall = float(input(f'    Enter the rainfall for {m}: '))
                if rainfall>0:
                    total = total+rainfall
                while rainfall<0:
                    print('    Invalid input; rainfall cannot be negative.')
                    rainfall = float(input(f'    Enter the rainfall for {m}: '))
                    if rainfall>0:
                        total = total+rainfall
        print(f'There are {month} months.') #output
        print(f'The total rainfall was {total:.2f} inches.')
        avg = total/month #calculate average
        print(f'The monthly average rainfall was {avg:.2f} inches.')
"""Do not change anything below this line."""
if __name__ == "__main__":
    main()