"""
  79. Word Search
  [ Medium ] | [ 40.2% ] -- Solved 26/03/2023 -- [ Array, Backtracking, Matrix ]

  Problem Statement:
  - Return whether the given word exists in the matrix as a sequence of adjacent tiles (not diagonal)
  - Same cell may not be used more than once

  Approach:
  - Simple DFS traversal, lay markers on the tiles in the current path so that they aren't reused in the same path
"""

from collections import Counter
from itertools import chain


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
        target, board, ly, lx = len(word), board, len(board), len(board[0]) if board else 0

        # Optional: These are hacks that exploit the nature of the testcases to rule out impossible scenarios / inform the start of the search
        if len(word) > ly * lx: return False
        if not (cnt := Counter(word)) <= Counter(chain(*board)):
            return False
        cnt = Counter(word)
        if cnt[word[0]] > cnt[word[-1]]:
            word = word[::-1]

        def recurse(cx, cy, cidx):
            cell = board[cy][cx]
            board[cy][cx] = None
            for direction in directions:
                ncx, ncy, nidx = cx + direction[0], cy + direction[1], cidx + 1
                if nidx == target or (0 <= ncx < lx and 0 <= ncy < ly and
                                      (board[ncy][ncx] == word[nidx] and recurse(ncx, ncy, nidx))):
                    return True
            board[cy][cx] = cell
            return False

        for i in range(ly):
            for j in range(lx):
                if board[i][j] == word[0] and recurse(j, i, 0):
                    return True
        return False
