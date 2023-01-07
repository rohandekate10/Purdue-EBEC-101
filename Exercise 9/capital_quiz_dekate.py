"""
Author: Rohan Dekate, dekate@purdue.edu
Assignment: 09.1 - Capital Quiz
Date: 11/10/2022

Description:
    Quiz user about US states and ask capitals and provide scores.

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
def get_state_data():
    # loads state capital data from the provided file state_capitals.txt
    # return data as a dictionary with the state names as keys and the state capitals as values
    state_capital = {}
    state = []
    capital = []
    all_data = []
    with open('state_capitals.txt') as fo:
        for line in fo:
            line = line.strip('\n')
            line = line.split(', ')
            all_data.append(line)
    for elem in all_data:
        capital.append(elem[0])
        state.append(elem[1])
    for x in state:
        for y in capital:
            state_capital[x] = y
            capital.remove(y)
            break
    return state_capital
# Define a main function
def main():
    """Write your mainline logic below this line (then delete this line)."""
    # quiz the user by asking them to enter the capital for a particular state.
    state_data = get_state_data()
    count = 0
    correct_ans = 0
    q_state = []
    q_capital = []
    while len(state_data.keys())>0:
        s, c = random.choice(list(state_data.items()))
        user = input(f'What is the capital of {s} (enter 0 to quit)? ')
        count = count+1
        user = user.title()
        if user == '0':
            count = count-1
            break
        elif user == c:
            print('  That is correct!')
            correct_ans = correct_ans+1
            del state_data[s]
        else:
            print('  That is incorrect.')
            print(f"  The capital of {s} is {c}.")
    print(f'You answered {correct_ans} out of {count} questions correctly.')
"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
