"""
Author: Rohan Dekate, dekate@purdue.edu
Assignment: 07.2 - Number Analysis
Date: 10/17/2022

Description:
    collects ten floating point numbers from the
    user and returns them as a list. Calculate highest,
    lowest, total sum and average of the numbers in the list.

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
def get_number_list():
    new_list = [] # Declare empty list
    for i in range(10):
        # Add number entered by user to the empty list
        new_list.append(float(input(f'  number {i+1:2} of 10: ')))
    return new_list # Return new list
    

# Define a main function
def main():
    """Write your mainline logic below this line (then delete this line)."""
    print('Enter 10 numbers:') # Ask for user input
    # Call function
    new_list = get_number_list()
    #Display output
    print(f'Highest number: {max(new_list):.2f}')
    print(f'Lowest number: {min(new_list):.2f}')
    print(f'Total: {sum(new_list):.2f}')
    print(f'Average: {sum(new_list)/len(new_list):.2f}')


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
