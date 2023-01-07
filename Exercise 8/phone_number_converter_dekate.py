"""
Author: Rohan Dekate, dekate@purdue.edu
Assignment: 08.2 - Phone Number Converter
Date: 11/03/2022

Description:
    Returns the telephone number with any alphabetic characters 
    that appeared in the original translated into their numeric equivalent.

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
from curses.ascii import isdigit

digit_letter_map = 'ABC2DEF3GHI4JKL5MNO6PQRS7TUV8WXYZ9'

def convert_number(phone_string):
    remaining_numbers = []
    phone_string = phone_string.upper() # Handle both upper and lower case characters
    for letter in phone_string:
        if letter.isalpha() == False:
            remaining_numbers.append(letter) # Add numbers from the user string to a list
        else:
            index = digit_letter_map.find(letter)
            for idx in range(index,len(digit_letter_map)):
                character = digit_letter_map[idx]
                if character.isdigit() == True: # Find number corresponding to alphabet
                    number = character
                    remaining_numbers.append(number)
                    break
    return ''.join(remaining_numbers)

# Define a main function
def main():
    """Write your mainline logic below this line (then delete this line)."""
    # Collect a phone number from the user
    phone_number = input('Enter a telephone number: ')
    output = convert_number(phone_number)
    print(f'The phone number is {output}')
    
"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
