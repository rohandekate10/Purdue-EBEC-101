"""
Author: Rohan Dekate, dekate@purdue.edu
Assignment: 00.1 - Hello User
Date: 08/22/2022

Description:
    This program asks the user for their name and then greets them using their entered name.
    The variable used to store user input is name.
    f-strings formatting is used to display the output/greeting.

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
    # Create a variable to store the user input
    name = input('What is your name? ')
    # Display the user input with greeting
    print(f"Hello {name}!")


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
