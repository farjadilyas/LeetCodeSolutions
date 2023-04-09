"""
  51. N-Queens
  [ Hard ] | [ 64.3% ] -- Solved 9/04/2023 -- [ Array, Backtracking ]

  Problem Statement:
  - The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that
    no two queens attack each other.
  - Eg for n=4: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]

  Approach:
  - Simple 'guided' backtracking solution, use 3 boolean arrays, colMap, posDiagonalMap, negDiagonalMap to keep track
    of valid columns, valid positive diagonals (row increases with columns) and valid negative diagonals (row decreases
    as column increases)
  - These maps keep track of what 'lines' are unsafe since they fall within a queen's moves, and hence can be used
    to guide our traversal
  - To figure out what diagonal a cell is on, we use a property where to move a step along the diagonal, both the row
    and column changes by 1 (+ve or -ve). We can take advantage of this to come up with a formula where the result stays
    constant for cells that lie in the same diagonal.

  Diagonal resolution - Try these out for yourself on any cell, they map all diagonals to a number 0 - 2n-1:
  - posDiagonal - formula: row-column+(n-1) - n-1 is only necessary to map it to a non-negative array index
  - negDiagonal - formula: row+column
    - Intuition for arriving at formula for negative diagonal - posDiagonal formula works because if we move along the
      diagonal, the change to row cancels out the change to column since they are being subtracted
    - However, for negDiagonals, row decreases as column increases, to counteract that we can flip the direction of
      the column axis like this: row-(n-1-column)+(n-1) - we just need a consistent formula, doesn't matter which one
    - This formula simplifies to row+column

  Time Complexity: O(N!)
  Space Complexity: O(N)
"""

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        colMap = [False for _ in range(n)]
        posDiagonalMap = [False for _ in range(n + n - 1)]
        negDiagonalMap = [False for _ in range(n + n - 1)]
        currentResult = [None for _ in range(n)]

        def backtrack(row):
            if row >= n:
                r = []
                for crow in currentResult:
                    cr = ['.' for _ in range(n)]
                    cr[crow] = 'Q'
                    r.append(''.join(cr))
                res.append(r)
                return
            for i in range(n):
                posDiagonalIdx = row - i + n - 1
                negDiagonalIdx = row + i
                if colMap[i] or posDiagonalMap[posDiagonalIdx] or negDiagonalMap[negDiagonalIdx]:
                    continue
                colMap[i] = posDiagonalMap[posDiagonalIdx] = negDiagonalMap[negDiagonalIdx] = True
                currentResult[row] = i
                backtrack(row + 1)
                colMap[i] = posDiagonalMap[posDiagonalIdx] = negDiagonalMap[negDiagonalIdx] = False
        backtrack(0)
        return res
