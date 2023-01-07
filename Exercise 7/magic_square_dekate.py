"""
Author: Rohan Dekate, dekate@purdue.edu
Assignment: 07.4 - Magic Square
Date: 10/20/2022

Description:
    Check if the square is a Lo Shu magic square.

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
def print_square(square):
    # takes a two-dimensional list representing a 3 by
    # 3 grid of numbers as its argument and prints the grid showing the numbers in the square
    #print('Your square is:')
    #print()
    rows, cols = 3,3
    for r in range(rows):
        print(' ', end='')
        for c in range(cols):
            n = square[r][c]
            print(f'{n:2}', end='')
        print()

def row_addition(mat):
    row_sum = []
    for i in range(3):
        add = sum(mat[i][:])
        row_sum.append(add)
    return row_sum

def column_addition(mat):
  col_sum = []
  for i in range(len(mat)):
    col = [row[i] for row in mat]
    #print(col)
    add = sum([row[i] for row in mat]) 
    col_sum.append(add)
  return col_sum

def diagonal_addition(mat):
  diag_sum = []
  diag1=[]
  diag2=[]
  # Primary Diagonal
  for i in range(len(mat)):
    diag1.append(mat[i][i])
  diag_sum.append(sum(diag1))
  #Secondary Diagonal
  k = len(mat) - 1
  for i in range(len(mat)):
    diag2.append(mat[i][k])
    k -= 1
  diag_sum.append(sum(diag2))
  return diag_sum

def grid_check(mat):
  matrix_elem = []
  for i in range(len(mat)):
    for j in range(len(mat)):
      elem = mat[i][j]
      matrix_elem.append(elem)
  #print(matrix_elem)
  
  grid = range(1,10)
  unique = []
  for elem in matrix_elem:
    if elem not in unique:
      unique.append(elem)
  #print(len(unique))

  for item in unique:
    if item not in grid:
      grid_flag = False
      break
    else:
      grid_flag = True
      continue

  if len(unique)!=9:
      #print(len(unique))
      grid_flag = False      
  
  return grid_flag

def is_magic(square):
    # takes a similar two-dimensional list of numbers as its argument and returns
    # the boolean value True if the argument represents a Lo Shu magic square and False otherwise.
    check = 15
    # Check Row Sum
    rows = row_addition(square)
    for r in rows:
        if r!=check:
            row_flag = False
            break
        else:
            row_flag = True
            continue
    
    # Check Column Sum
    cols = column_addition(square)
    for c in cols:
        if c!=check:
            col_flag = False
            break
        else:
            col_flag = True
            continue
    
    # Check Diagonal Sum
    diag = diagonal_addition(square)
    for d in diag:
        if d!=check:
            diag_flag = False
            break
        else:
            diag_flag = True
            continue

    # Check for numbers 1 through 9
    grid_flag = grid_check(square)
        
    if row_flag & col_flag & diag_flag & grid_flag == True:
        flag = True
    else:
        flag = False
    return flag

# Define a main function
def main():
    """Write your mainline logic below this line (then delete this line)."""
    # determine if each of the provided squares are Lo Shu magic squares and display the results
    s1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    s2 = [[5, 5, 5], [5, 5, 5], [5, 5, 5]]
    s3 = [[4, 9, 2], [3, 5, 7], [8, 1, 6]]
    squares = [s1,s2,s3]
    for s in squares:
        print('Your square is:')
        print_square(s)
        flag = is_magic(s)
        if flag == True:
            print('It is a Lo Shu magic square!')
        else:
            print('It is not a Lo Shu magic square.')
        print()
"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
