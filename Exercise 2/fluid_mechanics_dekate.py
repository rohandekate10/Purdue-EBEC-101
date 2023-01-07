"""
Author: Rohan Dekate, dekate@purdue.edu
Assignment: 02.5 - Fluid Mechanics
Date: 09/09/2022

Description:
    Program to calculate Reynolds number based on user input of 
    velocity of flowing water, pipe diameter and water temperature.
    Kinematic viscosity is dependent on temperature.

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
    # Declare kinematic viscosity constant
    t_5 = 1.52*1e-6 
    t_20 = 1.00*1e-6
    t_50 = 5.54*1e-7
    # Ask for user input
    temp = int(input('Enter the temperature in °C as 5, 20, or 50: '))
    velocity = float(input('Enter the velocity of water in the pipe (m/s): '))
    dia = float(input("Enter the pipe's diameter (m): "))
    # Check for temerature to select viscosity value
    if temp == 5:
        visc = t_5
    elif temp == 20:
        visc = t_20
    elif temp == 50:
        visc = t_50
    R = (velocity*dia)/visc # Calculate Reynolds number
    print(f'At {temp:.1f}°C, the Reynolds number for flow at {velocity} m/s in a {dia} m diameter pipe is {R:.2e}.')
"""Do not change anything below this line."""
if __name__ == "__main__":
    main()