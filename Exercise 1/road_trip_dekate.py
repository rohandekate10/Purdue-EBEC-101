"""
Author: Rohan Dekate, dekate@purdue.edu
Assignment: 01.1 - Road Trip
Date: 08/29/2022

Description:
    Estimate the budget for fuel required for a road trip when the user
    enters the following information - 
    the distance in miles,
    the average price of fuel in dollars per gallon, and
    fuel efficieny of vehicle in miles per gallon

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
    # Print program message
    print('Road trip fuel cost estimator:')

    # Ask user for distance
    dist = int(input('  How far away is your destination (miles)? ')) 
    
    # Ask user for average fuel price
    avg_price = float(input('  What is the average price of gas (dollars per gallon)? '))
    
    # Ask user for vehicle's fuel efficiency
    fuel_eff = float(input('  What is the fuel efficiency of your vehicle (mpg)? '))
    
    # Calculate the cost of fuel
    cost = int((2*dist)*avg_price/fuel_eff) 

    print()
    # Print Output
    print(f'The fuel cost for this trip is approximately ${cost}.')

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
