"""
Author: Rohan Dekate, dekate@purdue.edu
Assignment: 01.2 - Interest
Date: 08/30/2022

Description:
    This program codes the formula for compound interest and outputs the future value (FV) by asking the user -
    Principal (P) or amount initially deposited
    Annual Rate of Interest (r)
    Number of times the interest is compunded in a year (n)
    Number of years (t)

    The formula is
    FV = P(1+r/n)^(nt)

    Note: User will enter interest rate (r) in % and it has to be divided by 100 within the program

    The output should have a precision of 2 decimal points with comma separated values and $ sign.


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
    # Begin program
    print('Enter the following parameters.')
    
    # Ask user for principal amount and store in P
    P = int(input('  The initial deposit? '))

    # Ask user for interest rate and store in r
    r = float(input('  The annual interest rate in percent? '))

    # Convert interest rate entered by user in %
    r = r/100

    # Ask user for compunding time in years and store in t
    t = float(input('  The number of years the account earn interest? '))

    # Ask user for number of times interest is compounded in a year and store in n
    n = int(input('  The number of times interest is compounded each year: '))
    
    # Calculate Future Value
    FV = P*(1+r/n)**(n*t)

    # Output result as specified in description
    print(f'The balance of this account will be ${FV:,.2f} after {t} years.')

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()