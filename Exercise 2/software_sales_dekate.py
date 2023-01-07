"""
Author: Rohan Dekate, dekate@purdue.edu
Assignment: 02.2 - Software Sales
Date: 09/07/2022

Description:
    This program calculates the total amount after discount when a user enters the
    quantity of packages. The package's retail cost is $880. Discounts are offered 
    in tiered manner based on quantity entered by the user.
    The program displays if a valid quantity is input by the user.
    What is the % discount that the user is eligible for and the total cost.

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
    quantity = int(input('How many packages will be purchased: ')) # Ask for user input
    P = 880 # Price of one package
    # Create variables for discount rates
    D1 = 10 
    D2 = 15 
    D3 = 30 
    D4 = 42 
    # Conditional statements
    if quantity < 0:
        print('  Invalid Input!')
    elif quantity <4:
        print('  No discount applied.')
        total = P*quantity
        print(f'  The total price to purchase {quantity} packages is ${total:,.2f}.')
    elif quantity>=4 and quantity<=39:
        d = D1
        print(f'  {d}% discount applied.')
        total = P*quantity*((100-d)/100)
        print(f'  The total price to purchase {quantity} packages is ${total:,.2f}.')
    elif quantity>=40 and quantity<=199:
        d = D2
        print(f'  {d}% discount applied.')
        total = P*quantity*((100-d)/100)
        print(f'  The total price to purchase {quantity} packages is ${total:,.2f}.')
    elif quantity>=200 and quantity<=999:
        d = D3
        print(f'  {d}% discount applied.')
        total = P*quantity*((100-d)/100)
        print(f'  The total price to purchase {quantity} packages is ${total:,.2f}.')
    elif quantity>=1000:
        d = D4
        print(f'  {d}% discount applied.')
        total = P*quantity*((100-d)/100)
        print(f'  The total price to purchase {quantity} packages is ${total:,.2f}.')
"""Do not change anything below this line."""
if __name__ == "__main__":
    main()