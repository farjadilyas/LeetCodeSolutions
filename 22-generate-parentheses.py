"""
  153. Find Minimum in Rotated Sorted Array
  [ Medium ] | [ 48.2% ] -- Solved 31/07/2022 -- [ Array, Binary Search ]

  Problem Statement:
  - Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

  Approach:
  - Most obvious way to generate combinations is to traverse the tree of combinations via DFS
  - Use some conditions to limit the tree to only possibly valid combos
    - Only allow adding opening bracket if it is available
    - Only allow adding closing bracket if there is some available matching opening bracket
"""

def generateParenthesis(self, n: int) -> List[str]:
    ans = []
    def recurs(cur, o, c):
        if n == c:
            return ans.append(cur)
        if o < n:
            recurs(cur+'(', o+1, c)
        if o-c > 0:
            recurs(cur+')', o, c+1)
    recurs('', 0, 0)
    return ans