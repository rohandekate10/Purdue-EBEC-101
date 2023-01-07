"""
Author: Rohan Dekate, dekate@purdue.edu
Assignment: 09.4 - File Analysis
Date: 11/11/2022

Description:
    Process the two provided text files and generate
    new text files with frequency, common words data.
    Create 4 text files and store the information.

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
import string

"""Write new functions below this line (starting with unit 4)."""
# Function to read text file
def txt_file_reader(filename):
        punctuation = string.punctuation
        list_of_words = []
        with open(filename) as fo:
            for line in fo:
                line = line.lower()
                words = line.split()
                for w in words:
                    w = w.strip(punctuation)
                    list_of_words.append(w)
        return list_of_words
# Function to create dictionary from text file and count each word
def make_dict(list_of_words):
    dictionary = {}
    for w in list_of_words:
        if w not in dictionary:
            count = list_of_words.count(w)
            dictionary[w] = count
    return dictionary

# Define a main function
def main():
    """Write your mainline logic below this line (then delete this line)."""
    # Call functions on python_1.txt
    python_1 = txt_file_reader('python_1.txt')    
    dict_python_1 = make_dict(python_1)
    # Call functions on python_2.txt
    python_2 = txt_file_reader('python_2.txt')    
    dict_python_2 = make_dict(python_2)
    # Write word frequency text file
    temp = sorted(dict_python_1.items())
    for word,count in temp:
        with open('python_1_word_frequency.txt', 'a') as fo:
            fo.write(word + ': ' + str(count)+ '\n')

    temp = sorted(dict_python_2.items())
    for word,count in temp:
        with open('python_2_word_frequency.txt', 'a') as fo:
            fo.write(word + ': ' + str(count)+ '\n')
    # Common words, either or but not both words
    set_python_1 = set(dict_python_1.keys())
    set_python_2 = set(dict_python_2.keys())
    
    common_list = list(set_python_1.intersection(set_python_2))
    temp1 = common_list.sort()
    union_list = list(set_python_1 ^ set_python_2)
    temp2 = union_list.sort()

    for common in common_list:
        with open('common_words.txt', 'a') as fo:
            fo.write(common + '\n')

    for w in union_list:
       with open('eitherbutnotboth.txt', 'a') as fo:
            fo.write(w + '\n')
    
"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
