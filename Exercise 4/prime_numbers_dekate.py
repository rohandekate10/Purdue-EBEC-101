"""
Author: Rohan Dekate, dekate@purdue.edu
Assignment: 04.4 - Prime Numbers
Date: 09/22/2022

Description:
    A Boolean function named is_prime which takes an integer 
    as an argument and returns True if the argument is a prime number,
    or False otherwise.

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
import math
"""Write new functions below this line (starting with unit 4)."""
# Check if number is prime
def is_prime(x):
    if x>1: # Check only if input >1
        if x==2: # Special case of 2
            return True
        else:
            for i in range(2,int(x**0.5)+1): # Check for numbers for divisibility between 2 and square root of the number
                if (x%i)==0:
                    return False
            return x,True    
    return False

# Define a main function
def main():
    """Write your mainline logic below this line (then delete this line)."""
    num = int(input('Enter a positive integer (-1 to quit): ')) # Ask for user input
    while num !=-1: # Check if input is valid
        bool = is_prime(num) # Call function
        if bool == False:
            print(f'  {num} is not prime.')
        else:
            print(f'  {num} is prime!')
        num = int(input('Enter a positive integer (-1 to quit): ')) # Ask for user input

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()