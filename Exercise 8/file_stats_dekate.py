"""
Author: Rohan Dekate, dekate@purdue.edu
Assignment: 08.3 - File Stats
Date: 10/31/2022

Description:
    Reads the contents of a file and determine the number of words
    in the file, the number of lines in the file, 
    and average number of words per line.

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
    # Read the frontiero_v_richardson.txt file
    file = []
    with open('frontiero_v_richardson.txt') as fo:
        for line in fo:
            file.append(line.rstrip())
    total = 0
    num_lines = 0
    # Calculate File Statistics
    for line in file:
        temp = line.split()
        words = len(temp)
        total = total+words
        num_lines = num_lines+1
    # Display Output
    print(f"Total number of words: {total}")
    print(f"Total number of lines: {num_lines}")
    avg = total/num_lines
    print(f"Average number of words per line: {avg:.1f}")

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
