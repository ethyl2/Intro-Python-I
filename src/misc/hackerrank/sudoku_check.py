"""
https://app.codesignal.com/interview-practice/task/SKZ45AF99NpbnvgTn/description

Given 9 x 9 grid
Each char is either a digit '1' to '9' or a period '.'
Check whether each col,
each row,
each of 9 3x3 subgrids 
ALL contain all of the nums 1-9 once. -> Looks like all numbers do not have to be there, but can't have duplicates.
Note: the puzzle represented by grid does not have to be solvable.

grid = [['.', '.', '.', '1', '4', '.', '.', '2', '.'],
        ['.', '.', '6', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '1', '.', '.', '.', '.', '.', '.'],
        ['.', '6', '7', '.', '.', '.', '.', '.', '9'],
        ['.', '.', '.', '.', '.', '.', '8', '1', '.'],
        ['.', '3', '.', '.', '.', '.', '.', '.', '6'],
        ['.', '.', '.', '.', '.', '7', '.', '.', '.'],
        ['.', '.', '.', '5', '.', '.', '.', '7', '.']]
return True

grid = [['.', '.', '.', '.', '2', '.', '.', '9', '.'],
        ['.', '.', '.', '.', '6', '.', '.', '.', '.'],
        ['7', '1', '.', '.', '7', '5', '.', '.', '.'],
        ['.', '7', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '8', '3', '.', '.', '.'],
        ['.', '.', '8', '.', '.', '7', '.', '6', '.'],
        ['.', '.', '.', '.', '.', '2', '.', '.', '.'],
        ['.', '1', '.', '2', '.', '.', '.', '.', '.'],
        ['.', '2', '.', '.', '3', '.', '.', '.', '.']]
return False b/c 2 1s in 2nd col.
"""


def sudoku2(grid):
    # First, check rows.
    # Make a lookup dict.
    # If value of lookup dict is already 1, return False

    for i in range(len(grid)):
        lookup = {}
        for j in range(len(grid[i])):
            if grid[i][j] in lookup and grid[i][j] != '.':
                return False
            else:
                lookup[grid[i][j]] = 1
    return True
    # Next, check cols
    # Finally, check subgrids


grid1 = [['.', '.', '.', '1', '4', '.', '.', '2', '.'],
         ['.', '.', '6', '.', '.', '.', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
         ['.', '.', '1', '.', '.', '.', '.', '.', '.'],
         ['.', '6', '7', '.', '.', '.', '.', '.', '9'],
         ['.', '.', '.', '.', '.', '.', '8', '1', '.'],
         ['.', '3', '.', '.', '.', '.', '.', '.', '6'],
         ['.', '.', '.', '.', '.', '7', '.', '.', '.'],
         ['.', '.', '.', '5', '.', '.', '.', '7', '.']]

print(sudoku2(grid1))
