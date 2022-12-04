"""
  70. Climbing Stairs
  [ Easy ] | [ 51.7% ] -- Solved 16/10/2022 -- [ Dynamic Programming ]
  ---------- {{ SUBMISSION STATS }} ---------------
  FASTER THAN: 97.02%
  MEMORY USAGE: 96%

  Problem:
  - You are climbing a staircase. It takes n steps to reach the top.
  - Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

  Approach:
  - If there are m ways to reach two steps back, there are m ways to reach the current step by taking 2 steps
  - If there are n ways to reach one step back, there are n ways to reach the current step by taking 1 step
  - The two ways won't have any overlap.. simply because the last step is different, and there is no other way to
    reach the current step

  Time Complexity: O(N)
  Space Complexity: O(1)
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        """
        dp[n] = dp[n-2] (Climb two) + dp[n-1] (Climb one)

        1 = ->1
        2 = ->1->1, ->2
        3 = ->1->1->1 | ->1->2 | ->2->1
        4 = (->1->1->2 | ->2->2) | (->1->1->1->1 | ->1->2->1 | ->2->1->1)
        """
        if n < 3:
            return n
        two_back = 1
        one_back = 2
        for _ in range(n - 2):
            one_back += two_back
            two_back = one_back - two_back
        return one_back
