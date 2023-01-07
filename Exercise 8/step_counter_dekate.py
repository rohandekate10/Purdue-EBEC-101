"""
Author: Rohan Dekate, dekate@purdue.edu
Assignment: 08.6 - Step Counter
Date: 10/31/2022

Description:
    Read the steps.txt file. 
    Calculate and displays the average number of steps taken for each month.

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
    # Read the steps.txt file
    steps = []
    with open('steps.txt') as fo:
        for line in fo:
            steps.append(line.rstrip())
    # Create lists
    month = ['January','February','March','April','May','June','July','August','September','October','November','December']
    days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]
    average = []
    # Make calculations
    for d in days_in_month:
        total = 0
        slice_of_steps_monthly = steps[0:d]
        for s in slice_of_steps_monthly:
            s = int(s)
            total = total+s
        avg = total/d
        average.append(avg)
        del steps[0:d]
    # Display output
    print('The average steps taken each month were:')
    for m,avg in zip(month,average):
        print(f'{m:>10} : {avg:.2f}')


    
"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
