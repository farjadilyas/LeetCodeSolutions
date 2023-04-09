"""
  200. Number of Islands
  [ Medium ] | [ 57.0% ] -- Solved 9/04/2023 -- [ Array, DFS, BFS, Matrix, Union Find ]

  Problem Statement:
  - Given an m x n 2D binary grid which represents a map of '1's (land) and '0's (water),
    return the number of islands - assume the array is surrounded by water (0's)

  Approach:
  - Loop over the array, if the element is land, pick it as a starting point
  - Use DFS to mark the entire island as water and count it as an island
  - Repeat with other starting points

  Time Complexity: O(MN)
  Space Complexity: O(MN)
"""

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        lx = len(grid)
        ly = len(grid[0])
        def recurse(x, y):
            grid[x][y] = '0'
            if x+1 < lx and grid[x+1][y] == '1':
                recurse(x+1, y)
            if y+1 < ly and grid[x][y+1] == '1':
                recurse(x, y+1)
            if 0 <= x-1 and grid[x-1][y] == '1':
                recurse(x-1, y)
            if 0 <= y-1 and grid[x][y-1] == '1':
                recurse(x, y-1)
        islands = 0
        for xidx in range(lx):
            for yidx in range(ly):
                if grid[xidx][yidx] == '1':
                    recurse(xidx, yidx)
                    islands += 1
        return islands
