"""
Author: Rohan Dekate, dekate@purdue.edu
Assignment: 09.3 - Course Info
Date: 11/03/2022

Description:
    Create a dictionary of course data. Return the dictionary.
    As per user query display the room, instructor and time from
    the dictionary.

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
# Create and return dictionary
def get_course_data(): 
    fake_course_data = {'CS101':{'room':'3004', 'instructor': 'Django', 'time':'9:00 a.m.'},
                        'CS102':{'room':'4501', 'instructor': 'Idle', 'time':'10:00 a.m.'},
                        'CS103':{'room':'6755', 'instructor': 'Rich', 'time':'11:00 a.m.'},
                        'NT110':{'room':'1244', 'instructor': 'Marshal', 'time':'12:00 p.m.'},
                        'CM241':{'room':'1411', 'instructor': 'Pickle', 'time':'2:00 p.m.'}}
    return fake_course_data

# Define a main function
def main():
    """Write your mainline logic below this line (then delete this line)."""
    course_data = get_course_data()
    user = input('Enter a course number: ')
    # Check if user input exists in the dictionary keys
    # Display output
    if user in course_data.keys():
        print(f'  The details for course {user} are:')
        inner_dict = course_data[user]
        print(f"    Instructor: {inner_dict['instructor']}")
        print(f"          Room: {inner_dict['room']}")
        print(f"          Time: {inner_dict['time']}")
    else:
        print(f"  {user} is an invalid course number.")

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
