"""
  130. Surrounded Regions
  [ Medium ] | [ 36.8% ] -- Solved 10/04/2023 -- [ Array, BFS, DFS, Union Find, Matrix ]

  Problem Statement:
  - Check it out online

  Approach:
  - The only way a blob of 0's is not entirely surrounded by X's is if some part of it reaches the border, else, it will
    definitely be entirely surrounded on all 4 fronts by X's
  - So.. start DFS from the 4 borders of the matrix, mark every reachable 'O' as visited
  - All O's that are surrounded by X's will be unreachable ofc, so after conducting all the DFS traversals
  - Flip the O's that haven't been visited

  Optimization:
  - Mark visited O's in place on the board to save memory (can't get better than this in terms of memory)

  Time Complexity: O(NM)
  Space Complexity: O(NM)
"""

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        lx, ly = len(board), len(board[0])
        def dfs(x, y):
            if not (0 <= x < lx and 0 <= y < ly and board[x][y] == 'O'):
                return
            board[x][y] = None
            dfs(x, y+1)
            dfs(x+1, y)
            dfs(x, y-1)
            dfs(x-1, y)

        for xidx in range(lx):
            dfs(xidx, 0)
            dfs(xidx, ly-1)
        for yidx in range(ly):
            dfs(0, yidx)
            dfs(lx-1, yidx)
        for xidx in range(lx):
            for yidx in range(ly):
                if board[xidx][yidx] == 'O':
                    board[xidx][yidx] = 'X'
                elif board[xidx][yidx] is None:
                    board[xidx][yidx] = 'O'
