"""
Author: Rohan Dekate, dekate@purdue.edu
Assignment: 08.4 - Number Writer
Date: 10/31/2022

Description:
    Generate random numbers and write to a text file.
    Random numbers should be in the range [1019,1215]

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
from random import randrange

"""Write new functions below this line (starting with unit 4)."""

# Define a main function
def main():
    """Write your mainline logic below this line (then delete this line)."""
    # ask the user how many numbers to generate
    user = int(input('How many numbers would you like? '))
    # Write random numbers to a file named random_numbers.txt
    # Each random number should be in the range of 1019 through 1215 inclusive.
    write = []
    for num in range(0,user):
        random_number = randrange(1019, 1216)
        random_number = str(random_number) + '\n'
        write.append(random_number)
    #print(write)
    with open('random_numbers.txt', 'w') as fo:
        fo.writelines(write)
    
"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
