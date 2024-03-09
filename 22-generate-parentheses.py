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


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack, result = [], []
        op, cl = '(', ')'

        def form(num_pairs_allowed, num_pairs_open):
            if not num_pairs_allowed and not num_pairs_open:
                result.append(''.join(stack))

            if num_pairs_allowed:
                stack.append(op)
                form(num_pairs_allowed - 1, num_pairs_open + 1)
                stack.pop()
            if num_pairs_open:
                stack.append(cl)
                form(num_pairs_allowed, num_pairs_open - 1)
                stack.pop()

        form(n, 0)
        return result
