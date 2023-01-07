"""
Author: Rohan Dekate, dekate@purdue.edu
Assignment: 04.3 - Avg Grade
Date: 09/25/2022

Description:
    Ask the user to enter a valid score five times.
    Evaluate the grade and calculate the average.
    Display the grade for each score and the average score.

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
# Define function
def get_valid_score():
    score = float(input('Enter a score: ')) # Ask for user input
    while score < 0 or score > 100: # Invalid Input Check
        print('  Invalid Input. Please try again.') 
        score = float(input('Enter a score: '))
    return score # return valid score to main function

def calc_average(ListofScores): # Calculate average score from list
    total = 0
    for i in ListofScores:
        total = total+i
    average = total/len(ListofScores)
    return average # Return average

def determine_grade(x): # Evaluate grade based on an input score
    if x>=92 and x<=100:
        grade = 'A'
    elif x>=82 and x<92:
        grade = 'B'
    elif x>=73 and x<82:
        grade = 'C'
    elif x>=64 and x<73:
        grade='D'
    elif x>=0 and x<64:
        grade= 'F'
    return grade

# Define a main function
def main():
    """Write your mainline logic below this line (then delete this line)."""
    score_list = [] # Initialize a list to store valid scores
    num = 1 
    while num <=5: # Call functions
        score = get_valid_score()
        score_list.append(score)
        grade = determine_grade(score)
        print(f'  The letter grade for {score:.1f} is {grade}.')
        num = num+1
    avg = calc_average(score_list)
    final_grade = determine_grade(avg)
    print() # Display final output
    print('Results:')
    print(f'  The average score is {avg:.2f}.')
    print(f'  The letter grade for {avg:.2f} is {final_grade}.')

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
