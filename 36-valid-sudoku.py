"""
  36. Valid Sudoku
  [ Medium ] | [ 57.7% ] -- Solved 04/12/2022
  ----------- {{ SUBMISSION STATS }} --------------
  FASTER THAN: 92.40%
  MEMORY USAGE: 99.20%

  Problem:
  - Validate the given sudoku board based on the simple rules that no duplicate numbers should exist within any row,
    column, or square, where each number is between 1-9

  Approach:
  - Need to quickly look up in hash sets for row/col/box and index the particular cell
  - Since the domain is bounded, can use 3d array instead of hashset
  - (type, index, hasOccurred) - structure of lookup table - example [1][2][3] checks if the number 4 (counting from 0)
    occurs in the 3rd row

  Time Complexity: O(N)
  Space Complexity: O(N)
"""
from typing import List


def isValidSudoku(self, board: List[List[str]]) -> bool:
    tt = [[[False for _ in range(9)] for i in range(9)] for j in range(3)]
    for row in range(9):
        for col in range(9):
            if board[row][col] == '.':
                continue
            cnum = ord(board[row][col]) - 49
            if row < 3:
                bid = 0
            elif row < 6:
                bid = 3
            else:
                bid = 6
            if 3 <= col < 6:
                bid += 1
            elif col > 5:
                bid += 2
            if tt[0][bid][cnum] or tt[1][row][cnum] or tt[2][col][cnum]:
                return False
            tt[0][bid][cnum] = tt[1][row][cnum] = tt[2][col][cnum] = True
    return True


"""
  Here, we remove a dimension from the 3-d array we used to keep track of the row, col, box sets
  We replace the innermost dimension with numbers, and use bit manipulation to keep track of which numbers are in the
  set
  
  - When a number is encountered, create a mask for it using one-hot encoding
  - It already exists in a set if for eg: rowSet & valueMask != 0
  - To add it to a set, do this: rowSet |= valueMask
  
  - This decreases space used, and also practically decreases the runtime of this solution
"""


def isValidSudokuImp2(board: List[List[str]]) -> bool:
    rowSet, colSet, boxSet = ([0 for _ in range(9)] for i in range(3))
    for row in range(9):
        for col in range(9):
            if board[row][col] == '.':
                continue
            bid = (row - row % 3) + (col // 3)
            valueMask = 2 ** (ord(board[row][col]) - 49)
            if (rowSet[row] & valueMask) | (colSet[col] & valueMask) | (boxSet[bid] & valueMask):
                return False
            rowSet[row] |= valueMask
            colSet[col] |= valueMask
            boxSet[bid] |= valueMask
    return True
