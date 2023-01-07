"""
Author: Rohan Dekate, dekate@purdue.edu
Assignment: 03.1 - Cakes
Date: 09/15/2022

Description:
    Draw the ASCII art cake pattern as per user
    input of cake layers.

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
def main():
    """Write your mainline logic below this line (then delete this line)."""
    # Ask for user input
    layers = int(input('Enter the number of layers: '))
    # Loop that goes down
    for n in range(1,layers+1):
        print(' '*(layers-n) + '[',end='')
        for m in range(2*n-1): # Loop that goes sideways
            print('*',end='') 
        print(']')

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()