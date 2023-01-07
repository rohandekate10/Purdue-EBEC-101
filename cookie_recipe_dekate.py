"""
Author: Rohan Dekate, dekate@purdue.edu
Assignment: 01.3 - Cookie Recipe
Date: 08/29/2022

Description:
    A program to display quantity of ingredients (butter, sugar and flour) required as per the number of cookies a user wants to make.
    Given
    48 cookies require
    * 1.25 cups of butter
    * 1.5 cups of sugar
    * 2.5 cups of flour

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
    # Begin program. Ask user for number of cookies
    cookies = int(input('How many cookies do you want to make? '))
    
    # Calculate factor based on ingredient proportion for 48 cookies
    factor = cookies/48

    # Calculate quantity of butter
    butter = factor * 1.25

    #Calculate quantity of sugar
    sugar = factor * 1.5

    # Calculate quantity of flour
    flour = factor * 2.5

    # Ouput of the program
    print(f'To make {cookies:,} cookies, you will need:')
    print(f'{butter:>10,.2f} cups of butter')
    print(f'{sugar:>10,.2f} cups of sugar')
    print(f'{flour:>10,.2f} cups of flour')


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
