"""
  74. Search a 2D Matrix
  [ Medium ] | [ 45.8% ] -- Solved 30/07/2022 -- [ Binary Search, Matrix ]
  ----------- {{ SUBMISSION STATS }} --------------
  FASTER THAN: 96.80%
  MEMORY USAGE: 89.09%

  Problem Statement:
  - Given a 2D matrix that is sorted in ascending order, in row-major order, write an efficient algorithm to search for
    a number and return whether it is present or not

  Approach:
  - Since the matrix is effectively completely sorted, binary search can be used
  - Normal binary search, with the addition that the [row][col] indices have to be calculated this time since we are
    mapping from a 2D to a 1D Matrix
    - row = index/n
    - column = index%n

  Time Complexity: O(log(mn))
  Space Complexity: O(1)
"""


def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    start = 0
    n = len(matrix[0])
    end = (len(matrix) * n) - 1
    while True:
        middle = (start + end) >> 1
        middle_val = matrix[int(middle / n)][middle % n]
        if middle_val == target:
            return True
        elif middle_val < target:
            start = middle + 1
        else:
            end = middle - 1
        if end < start:
            return False
