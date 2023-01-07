"""
Author: Rohan Dekate, dekate@purdue.edu
Assignment: 07.1 - Multiples of N
Date: 10/17/2022

Description:
     function should return a new list containing
     the integers from its second argument which are 
     multiples of its first argument.

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
# Define multiples_of function
def multiples_of(integer, listofintegers):
    new_list = [] # Declare Empty list
    for num in listofintegers:
        if num%integer == 0: # Check if the number is a multiple of integer
            new_list.append(num) # Add the number to the empty list
    return new_list
    

# Define a main function
def main():
    """Write your mainline logic below this line (then delete this line)."""
    integer = 13 # Define integer
    listofintegers = [19, 1599, -546, 10, 39, -58, 1, 85, 201, -91, 286, 799, 406] # Define list
    # Display results
    print('Original list of numbers:')
    print(' ',listofintegers)
    new_list = multiples_of(integer, listofintegers)
    print('Numbers in the list that are multiples of 13:')
    print(' ',new_list)

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
