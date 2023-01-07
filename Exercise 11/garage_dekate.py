"""
Author: Rohan Dekate, dekate@purdue.edu
Assignment: 11.2 - Garage
Date: 11/14/2022

Description:
    

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
import random

"""Write new functions below this line (starting with unit 4)."""
class Garage:
    def __init__(self, name, spaces, cars):
        # The name attribute will store the name for the garage as a string
        self.name = name
        # the spaces attribute will be used to track the total number of spaces as an integer
        self.spaces = spaces
        # the cars attribute will track the number of cars currently in the garage as an integer
        self.cars = cars

    def car_in(self):
        '''This method should increment the cars attribute and print a success message if there
        are spaces available, otherwise it should print an error message.'''
        pass

    def car_out(self):
        '''This method should decrement the cars attribute and print a success message if
        there are cars in the garage, otherwise it should print an error message.'''
        pass

    def status(self):
        '''This method should print a status message stating how many empty spaces are avail-
        able in the garage.'''
        pass

# Define a main function
def main():
    """Write your mainline logic below this line (then delete this line)."""
    
"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
