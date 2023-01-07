"""
Author: Rohan Dekate, dekate@purdue.edu
Assignment: 10.3 - Covid 19 Cases
Date: 11/07/2022

Description:
    Reads the contents of the file and calculates the total 
    number of cases for each week

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
import datetime
import matplotlib.pyplot as plt

"""Write new functions below this line (starting with unit 4)."""

# Define a main function
def main():
    """Write your mainline logic below this line (then delete this line)."""
    #Loads indiana_covid-19_data_fall_2022.txt file
    first_date = []
    last_date = []
    number_of_new_cases = []
    number_of_new_deaths = []
    data = []
    with open('indiana_covid-19_data_fall_2022.txt') as fo:
        for line in fo:
            line = line.split()
            data.append(line)
    # Separate each column in the text file into a different list
    for l in data:
        first_date.append(l[0])
        last_date.append(l[1])
        number_of_new_cases.append(float(l[2]))
        number_of_new_deaths.append(float(l[3]))
    # Calculate rolling sum of new cases
    total_number_of_cases_each_week = []
    total_number_of_cases_each_week.append(0)
    for case in number_of_new_cases:
        total_number_of_cases_each_week.append(case+total_number_of_cases_each_week[-1])
    total_number_of_cases_each_week.pop(0)
    #print(total_number_of_cases_each_week)
    # Extract dates in datetime format
    dates = []
    for date in first_date:
        y, m, d = date.split('-')
        dt = datetime.date(int(y), int(m), int(d))
        #print(dt)
        dates.append(dt)
    #print(dates)
    # Make plots
    fig, ax = plt.subplots()
    # Change y-axis by dividing by 1000 so that the plot looks as per question
    ax.bar(dates, [i/1000 for i in total_number_of_cases_each_week], width = 7)
    ax.set_title('Weekly Positive COVID-19 Cases in Indiana')
    ax.set_xlabel('Date')
    ax.set_ylabel('Number of Cases (in thousands)')
    #ax.set_ylim(0,2000)
    fig.autofmt_xdate()
    plt.show()
"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
