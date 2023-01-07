"""
Author: Rohan Dekate, dekate@purdue.edu
Assignment: 08.5 - Number Reader
Date: 10/31/2022

Description:
    Read the random numbers from the random_numbers.txt file.
    Calculate and display the number/count,minimum,maximum,sum,average
    of the random numbers in the file. 

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
    # Read the random_numbers.txt file
    random_num = []
    with open('random_numbers.txt') as fo:
        for line in fo:
            random_num.append(line.rstrip())
    # Create new list to store integer values
    new_random_num = []            
    for num in random_num:
        num = int(num)
        new_random_num.append(num)
    #print(new_random_num)
    del random_num # Delete old list with string of random integers
    count = len(new_random_num)
    minimum = min(new_random_num)
    maximum = max(new_random_num)
    total = sum(new_random_num)
    average = total/count
    # Display Output
    print(f"{count:,} numbers were read from the file.")
    print(f"Min: {minimum:,}")
    print(f"Max: {maximum:,}")
    print(f"Sum: {total:,}")
    print(f"Avg: {average:,.1f}")


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
