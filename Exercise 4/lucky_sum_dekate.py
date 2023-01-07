"""
Author: Rohan Dekate, dekate@purdue.edu
Assignment: 04.2 - Lucky Sum
Date: 09/19/2022

Description:
    Function to calculate and return the sum of the “lucky numbers”,
    which are all of the numbers from the smallest argument to the 
    largest argument that are not divisible by 3.

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
# Define function
def lucky_sum(a,b):
    sum = 0
    if b<a:
        a,b = b,a
    for num in range(a,b+1,1):
        if num%3!=0:
            sum = sum+num
    return sum
# Define a main function
def main():
    """Write your mainline logic below this line (then delete this line)."""
    # Ask input from user
    num1 = int(input('Enter the first integer: '))
    num2 = int(input('Enter the second integer: '))    
    # Call function
    ans = lucky_sum(num1,num2)
    # Display output
    print(f'The sum of the lucky numbers is {ans:,}.')

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
