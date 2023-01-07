"""
Author: Rohan Dekate, dekate@purdue.edu
Assignment: 06.1 - Math Quiz
Date: 10/03/2022

Description:
    A function that return random integer values based on number
    of digits. The program check for the addition from the user.

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
import random as r # Import random module as alias r

"""Write new functions below this line (starting with unit 4)."""
# Define the function that returns random integer based on digits passed as argument
def random_number(digits):
    if digits == 2:
        num = r.randrange(10,100)
    elif digits == 3:
        num = r.randrange(100,1000)
    return num

# Define a main function
def main():
    """Write your mainline logic below this line (then delete this line)."""
    # Get the first random integer that is 2 digits
    A = random_number(2)
    # Get the second random integer that is 3 digits
    B = random_number(3)
    # Display the problem
    print(f'   {A}')
    print(f'+ {B}')
    print('-----')
    # Ask for user input for answer
    ans = int(input('= '))
    # Check if answer is correct
    if ans == A+B:
        print('Correct -- Good Work!')
    else:
        print(f'Incorrect. The correct answer is {A+B}.')

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
