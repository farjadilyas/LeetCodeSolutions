"""
  22. Generate Parentheses
  [ Medium ] | [ 74.3% ] -- Solved 31/07/2022 -- [ Array, Binary Search ]

  Problem Statement:
  - Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

  Approach:
  - Most obvious way to generate combinations is to traverse the tree of combinations via DFS
  - Use some conditions to limit the tree to only possibly valid combos
    - Only allow adding opening bracket if it is available
    - Only allow adding closing bracket if there is some available matching opening bracket

  Alternate Approach:
  - Note: this approach is not better, and in some ways (complexity, practical cost) worse that the previous one
  - Its possible to generate these parentheses using a formula with the same formulation as the Catalan Number formula
  - F(N) = "(" + F(I) + ")" + F(N-1-I) where I=1..N-1
  - Can simply write this as a recursive function
  - correlation here is that C(3), the 3rd Catalan number = number of ways parenthesis with 3 pairs of brackets can
    be formed
  - So F(N) = C(N) = 4^n / n*sqrt(n)

  Time Complexity: O(4^n / sqrt(n))
    - Explanation: number of valid parentheses strings with 'n' pairs is equal to the nth catalan numbers
    - nth catalan number is asymptotically bound by 4^n/(n*sqrt(n))
    - multiply the bound by n to represent the work done to construct (join) each string of length 2n, and also a max
      of 2n backtracking steps per arrangement
  Space Complexity: O(n) - max recursion depth is 2n
"""


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answer = []
        stack = []

        def form(num_opened, num_closed):
            if num_opened == num_closed == n:
                answer.append(''.join(stack))
            if num_opened < n:
                stack.append('(')
                form(num_opened+1, num_closed)
                stack.pop()
            if num_closed < num_opened:
                stack.append(')')
                form(num_opened, num_closed+1)
                stack.pop()
        form(0, 0)
        return answer
