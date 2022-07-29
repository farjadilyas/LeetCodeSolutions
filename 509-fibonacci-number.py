"""
  509. Fibonacci Number
  [ Easy ] | [ 69.1% ] -- Solved 26/07/2022 -- [ Dynamic Programming ]

  Problem:
  - Output Nth Fibonacci number

  Approach:
  - Memoization to remember results & only need to remember last 2 results

  Time Complexity: O(N)
  Space Complexity: O(1)
"""


def fib(self, n):
    if n == 0:
        return 0
    cur = 1
    prev = 0
    for i in range(n - 1):
        temp = cur
        cur += prev
        prev = temp

    return cur
