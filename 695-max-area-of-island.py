"""
  695. Max Area of Islands
  [ Medium ] | [ 71.8% ] -- Solved 9/04/2023 -- [ Array, DFS, BFS, Matrix, Union Find ]

  Problem Statement:
  - Given an m x n 2D binary grid which represents a map of '1's (land) and '0's (water),
    return the area of the largest island - assume the array is surrounded by water (0's)

  Approach:
  - Similar to #200 - Number of islands
  - Loop over the array, if the element is land, pick it as a starting point
  - Use DFS to mark the entire island as water and track its area
  - Repeat with other starting points

  Time Complexity: O(MN)
  Space Complexity: O(MN)
"""

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        lx = len(grid)
        ly = len(grid[0])
        def recurse(x, y):
            grid[x][y] = 0
            res = 1
            if x+1 < lx and grid[x+1][y]:
                res += recurse(x+1, y)
            if y+1 < ly and grid[x][y+1]:
                res += recurse(x, y+1)
            if 0 <= x-1 and grid[x-1][y]:
                res += recurse(x-1, y)
            if 0 <= y-1 and grid[x][y-1]:
                res += recurse(x, y-1)
            return res
        marea = 0
        for xidx in range(lx):
            for yidx in range(ly):
                if grid[xidx][yidx]:
                    marea = max(recurse(xidx, yidx), marea)
        return marea
