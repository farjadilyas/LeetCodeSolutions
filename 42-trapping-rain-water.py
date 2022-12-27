"""
  42. Trapping Rain Water
  [ Hard ] | [ 58.9% ] -- Solved 25/12/2022
  Faster than: 90.5% | Less memory: 46.7%

  Problem:
  - Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much
    water it can trap after raining.

  APPROACH:
  - Very intuitive, similar to #11 - container with most water
  - Amount of water that can be held is the minimum of the heights of the two local maximas on either side of a point
  - Place two pointers on either end
  - Forward pass calculates how much water can be held assuming water doesn't drain from the other side
  - Backward pass does the same in the reverse direction
  - Taking the minimum of the results of the two passed gives how much water can be held if water can drain on either
    side, i.e, the final answer
  - The three passed can be combined into one with some conditions

  Time Complexity: O(N)
  Space Complexity: O(1)
"""


from math import ceil
def trap(self, height: List[int]) -> int:
    l = len(height)
    m = ceil(l / 2)
    ans = [None] * l

    total = backward_run = forward_run = backward_max = forward_max = 0
    for i in range(l):
        if height[i] >= forward_max:
            forward_run = forward_max = height[i]
            ans[i] = 0
        elif ans[i] is None:
            ans[i] = forward_run - height[i]
        else:
            ans[i] = min(forward_run - height[i], ans[i])
        if i >= m:
            total += ans[i]

        # Mirror of the forward logic
        j = l - i - 1
        if height[j] >= backward_max:
            backward_run = backward_max = height[j]
            ans[j] = 0
        elif ans[j] is None:
            ans[j] = backward_run - height[j]
        else:
            ans[j] = min(backward_run - height[j], ans[j])
        if j < m:
            total += ans[j]
    return total