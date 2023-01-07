"""
Author: Rohan Dekate, dekate@purdue.edu
Assignment: 10.2 - Gas Prices
Date: 11/07/2022

Description:
    Read the contents of the txt file, and use matplotlib to plot the
    data as a line graph.

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
import matplotlib.pyplot as plt

"""Write new functions below this line (starting with unit 4)."""

# Define a main function
def main():
    """Write your mainline logic below this line (then delete this line)."""
    #Loads 2008_Weekly_Gas_Averages.txt file
    price = []
    with open('2008_Weekly_Gas_Averages.txt') as fo:
        for line in fo:
            line = line.strip('\n')
            num = float(line)
            price.append(num)
    
    # Make list of week numbers
    week = []
    for w in range(1,len(price)+1):
        week.append(w)
    
    # Make pie plot from sales data in list    
    fig, ax = plt.subplots()
    ax.set_title('2008 Weekly Gas Prices') # Set title
    ax.plot(week,price) # Plot graph
    ax.set_xlabel('Weeks (by number)') # Set x-axis label
    ax.set_ylabel('Average Price (dollars/gallon)') # Set y-axis label
    ax.set_xlim(1,52) # Set y-axis limits
    ax.set_ylim(1.5,4.25) # Set x-axis limits
    ax.grid() # Plot grid
    plt.show()

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
