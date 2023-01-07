"""
Author: Rohan Dekate, dekate@purdue.edu
Assignment: 10.4 - Sin Cos
Date: 11/07/2022

Description:
    draw a plot of sine and cosine from 0 to 2π
    on the same axes.

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
import math

"""Write new functions below this line (starting with unit 4)."""

# Define a main function
def main():
    """Write your mainline logic below this line (then delete this line)."""
    sine = []
    cosine = []
    x = range(0,360)
    for angle in x:
        sine.append(math.sin(angle*(math.pi/180)))
        cosine.append(math.cos(angle*(math.pi/180)))
    #print(sine,cosine)
    fig, ax = plt.subplots()
    #x = [i/360 for i in x]
    ax.plot(x, sine, color = 'r')
    ax.plot(x, cosine, color = 'b')
    ax.set_ylim(-1.1,1.1)
    xlabels = ['$\\pi/2$', '$\\pi$', '$3\\pi/2$', '$2\\pi$']
    ax.set_xticks([90, 180, 270, 360])
    ax.set_yticks([-1,1])
    # xlabels = [90, 180, 270, 360]
    ax.set_xticklabels(xlabels)
    for spine in ['top', 'right']:
        ax.spines[spine].set_visible(False)
    for spine in ['bottom', 'left']:
        ax.spines[spine].set_position('zero')
    plt.show()
"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
