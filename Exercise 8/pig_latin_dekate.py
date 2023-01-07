"""
Author: Rohan Dekate, dekate@purdue.edu
Assignment: 08.1 - Pig Latin
Date: 10/27/2022

Description:
    Convert a string to Pig Latin.

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
from re import L

"""Write new functions below this line (starting with unit 4)."""
# Takes a string as its only argument and returns another string
# with each of the words from the first string converted into Pig Latin.
def pig(string): 
    new_string = []
    string = string.lower()
    string = string.split()
    suffix = 'ay'
    for letter in string:
        first_letter = letter[0]
        letter = letter.lstrip(first_letter)
        letter = letter+first_letter+suffix
        new_string.append(letter)
    new_string = ' '.join(new_string)
    new_string = new_string.capitalize()
    return new_string

# Define a main function
def main():
    """Write your mainline logic below this line (then delete this line)."""
    # Collect an input string from the user and display the converted result
    string = input('Enter a string: ')
    output = pig(string)
    print(f'Pig latin: {output}')
    
"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
