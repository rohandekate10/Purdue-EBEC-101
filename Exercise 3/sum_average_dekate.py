"""
Author: Rohan Dekate, dekate@purdue.edu
Assignment: 03.2 - Sum Average
Date: 09/12/2022

Description:
    Ask the user to input non-negative numbers. 
    Calculate sum and average and display. 
    If a negative number is entered then exit the program.

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
    num = float(input('Enter a non-negative number (negative to quit): '))
    sum = 0
    i = 0
    # Exit if first number is negative
    if num<0:
        print("  You didn't enter any numbers.")
    else:
        # Start loop
        while num>=0:
            sum = sum+num
            i = i+1
            num = float(input('Enter a non-negative number (negative to quit): '))
        # Calculate average
        avg = sum/i 
        # Display output
        print(f'  You entered {i} numbers.') 
        print(f'  Their sum is {sum:.3f} and their average is {avg:.3f}.')
        
"""Do not change anything below this line."""
if __name__ == "__main__":
    main()