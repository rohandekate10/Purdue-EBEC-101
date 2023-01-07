"""
Author: Rohan Dekate, dekate@purdue.edu
Assignment: 07.3 - Roll Analysis
Date: 10/20/2022

Description:
    Analyze distribution of 2 random dice rolls and 
    calculate the frequency.

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
def roll_d6():
    # returns a random integer between 1 and 6 (inclusive)
    r = random.randint(1, 6)
    return r

def get_2d6_rolls(num_rolls):
    # uses roll_d6 function to simulate rolling two six sided dice multiple times
    d6_2_rolls = []
    for r in range(num_rolls):
        r1 = roll_d6()
        r2 = roll_d6()
        d6_2_rolls.append(r1+r2)
    return d6_2_rolls

# Define a main function
def main():
    """Write your mainline logic below this line (then delete this line)."""
    #call your get_2d6_rolls function to simulate 1,000,000 rolls
    result = get_2d6_rolls(1000000)
    # Use the list returned from this function call to calculate and print
    # the percentage of rolls that have each value between 2 and 12.
    frequency = []
    for num in range(2,13):
        counts = result.count(num)
        percent = (counts*100)/1000000
        frequency.append(percent)
    # Display Output
    roll = list(range(2,13))
    print('Roll  Frequency')
    for r,freq in zip(roll, frequency):
        print(f'{r:3}  {freq:7.2f}%')

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
