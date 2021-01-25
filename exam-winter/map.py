import sys
# from typing import Tuple, List, Set, Optional

# LOOK: SMILES AND OTHER SYMBOLS DOESN'T DISPLAY ON TERMINAL CHANGED TO NUMBERS FOR EASE
def change_to_num(digits):

    for n, i in enumerate(digits):
        if i == u'\u2612':
            digits[n] = 0
        if i == u'\u263a':
            digits[n] = 1
        if i == u'\u263c':
            digits[n] = 2
        if i == u'.':
            digits[n] = 3

    return digits

def reverse_change_to_num(digits):

    for n, i in enumerate(digits):
        if i == 0:
            digits[n] = u'\u2612'
        if i == 1:
            digits[n] = u'\u263a'
        if i == 2:
            digits[n] = u'\u263c'
        if i == 3:
            digits[n] = u'.'

    return digits    




def read(filename):
    digits = [i for ele in filename.read().decode('utf-8') for i in ele ]
    digits = [value for value in digits if value != '\n']

    digits = change_to_num(digits)

    grid = group(digits, 7)
    # print(len(digits))
    # print(grid)
    return grid

def group(values, n) :

    splited = [values[i::n] for i in range(n)]
    return splited

 
def isPath(matrix, n):
 
    # Defining visited array to keep
    # track of already visited indexes
    visited = [[False for x in range (n)]
                      for y in range (n)]
    

    flag = False
 
    for i in range (n):
        for j in range (n):
           

            if (matrix[i][j] == 1 and not visited[i][j]):
 
                if (checkPath(matrix, i, 
                              j, visited)):

                    flag = True
                    break
    if (flag):
        print("path exist")
        for i in range (n):
            for j in range (n):
                if visited[i][j]:
                    if matrix [i][j] == 2:
                        pass
                    else:
                        matrix [i][j] = 1
 
    else:

        print("path not exist")
    
    print("RESULT:")
    for x in matrix:
        print(x)

def isSafe(i, j, matrix):
   
    if (i >= 0 and i < len(matrix) and
        j >= 0 and j < len(matrix[0])):
        return True
    return False
 
# Returns true if there is a path from a source
def checkPath(matrix, i, j,
              visited):
 
    # Checking the boundries, walls and
    # whether the cell is unvisited
    if (isSafe(i, j, matrix) and
        matrix[i][j] != 0 and not
        visited[i][j]):
       
        # Make the cell visited
        visited[i][j] = True
 
        # If the cell is the required
        # destination then return true
        if (matrix[i][j] == 2):
           return True
 
        # traverse up
        up = checkPath(matrix, i - 1,
                       j, visited)
 
        # If path is found in up
        # direction return true
        if (up):
           return True
 
        # Traverse left
        left = checkPath(matrix, i, 
                         j - 1, visited)

        if (left):
           return True
 
        # Traverse down
        down = checkPath(matrix, i + 1, j, visited)
 
        if (down):
           return True
 

        right = checkPath(matrix, i, 
                          j + 1, visited)
 

        if (right):
           return True
     
    
    # No path detected
    return False



if __name__ == "__main__":
    with open(sys.argv[1], 'r') as my_file:
        # print(my_file.read())
        grid = read(my_file)
        # for x in grid:
        #     print(x)
        # LOOK: SMILES AND OTHER SYMBOLS DOESN'T DISPLAY ON TERMINAL CHANGED TO NUMBERS FOR EASE
        if isPath(grid, 7) == False:
            print("no path")
