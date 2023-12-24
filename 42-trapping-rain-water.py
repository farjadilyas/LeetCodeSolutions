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
  Space Complexity: O(N) - array for storing forward pass values
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


"""
  OPTIMAL SOLUTION - O(N) time - O(1) space
  - Two pointer solution
  - Two pointers point to the edge of the left and right subset that have had their solutions calculated
  - Every move of a pointer finds the solution for the new position the pointer points to
  
  - Start with two pointers on 0 and N-1
  - Let leftMax hold the max value pointed to by leftPtr so far, same for rightMax
  - Move the pointer with the smaller value forward
  - EXPLANATION:
    - lets say left subarray is [0,1,2] and right subarray is [3,1]
    - left ptr at two should move forward because the formula for the answer at leftPtr+1 is:
      - min(leftMax, rightMax) - height[i]
      - if left ptr moves forward..
        - we know leftMax for i for sure (no elements left)
        - leftPtr would only move to the right if the right side had a bigger element
        - hence: rightMax > leftMax -> min(leftMax, rightMax) = leftMax
        - hence we know all we need to calculate the answer for the new leftPtr position
  - Once you have moved one of the pointers, make sure to update the respective max for the Ptr
  
  KEY INSIGHT:
  - First its important to realise the formula for the answer at a point
  - ans[i] = min(leftMax, rightMax) - height[i]
  - We needed the space since we could keep one running total w.r.t the iteration, but the total in the other
    direction needed to be memoized
  - Using two pointers, we can reach the elements that are first limited by ONE OF the running totals so far
  - Realise that the limiting total will definitely be less than the potential total in the opp direction
    if we move the smaller pointer
  - Hence, we resolve the left and right total dependency in linear time without needing the opposing total memoized
"""


class Solution:
    def trap(self, height: List[int]) -> int:
        start, end = 0, len(height)-1
        leftMax, rightMax = height[start], height[end]
        ans = 0
        while start < end:
            if height[start] > height[end]:
                end -= 1
                ans += max(rightMax - height[end], 0)
                rightMax = max(rightMax, height[end])
            else:
                start += 1
                ans += max(leftMax - height[start], 0)
                leftMax = max(leftMax, height[start])
        return ans
