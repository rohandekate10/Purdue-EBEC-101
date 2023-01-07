"""
Author: Rohan Dekate, dekate@purdue.edu
Assignment: 09.2 - World Series
Date: 11/03/2022

Description:
    Load WorldSeriesWinners.txt file and create two dictionaries 
    of winners and number of times a team has won the world series.
    Query the dictionaries by entering a year for which winning 
    team's name and number of championships is required.

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


def load_winners_data(): 
    teams = []
    dict1 = {} 
    dict2 = {} 

    years = list(range(1903, 2022,1))
    years.remove(1904)
    years.remove(1994)
    
    #Loads WorldSeriesWinners.txt file
    with open('WorldSeriesWinners.txt') as fo:
        for line in fo:
            line = line.strip('\n')
            teams.append(line)
    
    for x,y in zip(teams, years):
        dict2[y] = x

    for x in teams:
        count = teams.count(x)
        dict1[x] = count
    
    return dict1, dict2

# Define a main function
def main():
    """Write your mainline logic below this line (then delete this line)."""
    dict1, dict2 = load_winners_data()
    user = int(input('Enter a year in the range 1903 -- 2021: '))
    # program should display the name of the team that won the World Series that year
    if user == 1904 or user == 1994:
        print(f"  The World Series wasn't played in the year {user}.")
    elif user in dict2:
        winning_team = dict2[user]
        print(f'  The {winning_team} won the World Series in {user}.')
        times = dict1[winning_team]
        print(f"  They have won the World Series {times} times.")
    else:
        print(f"  Data for the year {user} is not included in this system.")

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
