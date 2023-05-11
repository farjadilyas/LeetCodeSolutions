"""
  994. Rotting Oranges
  [ Medium ] | [ 53.0% ] -- Solved 10/04/2023 -- [ Array, BFS, Matrix ]

  Problem Statement:
  - 0 - empty cell, 1 - fresh orange, 2 - rotten orange
  - Every minute, a rotten orange turns the oranges directly adjacent to it (1 step away) rotten
  - Find the minimum number of minutes it will take to make all oranges rotten, return -1 if it isn't possible
    (some fresh orange doesn't have a path to a rotten one)

  Approach:
  - This is a classic BFS problem, fits its approach perfectly
  - Starting points are scattered, they 'spread out' and we want to measure the steps
  - Loop over the grid, store rotten coords in queue
  - Conduct BFS using the queue, use None to mark the end of a level to allow us to count iterations/'minutes'
  - Also count the number of fresh oranges at the start, they should be zeroed by the end, else return -1

  Time Complexity: O(NM)
  Space Complexity: O(NM)
"""

from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        lx, ly, queue, numFresh = len(grid), len(grid[0]), deque(), 0
        for xidx in range(lx):
            for yidx in range(ly):
                if grid[xidx][yidx] == 2:
                    queue.append((xidx, yidx))
                elif grid[xidx][yidx] == 1:
                    numFresh += 1
        queue.append(None)
        num_iter = 0
        while queue:
            e = queue.popleft()
            if e is None:
                num_iter += 1
                if queue:
                    queue.append(None)
                continue
            for direction in directions:
                nx, ny = e[0]+direction[0], e[1]+direction[1]
                if 0 <= nx < lx and 0 <= ny < ly and grid[nx][ny] == 1:
                    grid[nx][ny] = 2
                    numFresh -= 1
                    queue.append((nx, ny))
        return num_iter-1 if numFresh == 0 else -1
