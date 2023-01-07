"""
Author: Rohan Dekate, dekate@purdue.edu
Assignment: 11.1 - Dice
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
class Dice:
    def __init__(self, sides):
        self.sides = sides

    def roll(self):
        rand_int = random.randint(1, self.sides)
        #print(num_roll)
        return rand_int

    def n_rolls(self,times=10):
        print(f"Rolling a {self.sides} sided die {times} times: ", end = '')
        for t in range(times):
            #print(t)
            d = self.roll()
            if t < times-1:
                print(d, end = ',')
            else:
                print(d, end = '')
        print()

# Define a main function
def main():
    """Write your mainline logic below this line (then delete this line)."""
    six_sided_die = Dice(6)
    six_sided_die.n_rolls(10)

    ten_sided_die = Dice(10)
    ten_sided_die.n_rolls(10)

    twenty_sided_die = Dice(20)
    twenty_sided_die.n_rolls(10)
"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
