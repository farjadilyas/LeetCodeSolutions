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
