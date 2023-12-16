"""
  238. Product of Array except self
  [ Medium ] | [ 64.8% ] -- Solved 04/12/2022

  Problem:
  - Given an array, return an array where each element contains the product of all elements other than itself
  - Must solve it in O(N), and ideally in O(1) space complexity, excluding the space used by the result array

  APPROACH:
  - Every elements needs the sum to its left and right
  - A memoized running left total, and running right total, can provide running left and right totals at any point of
    the array
  - So result[i] = runningLeft[i-1] + runningRight[i+1]
  - To comply with O(1) space complexity, only use the results array for memoization
  - Memoize runningLeft, then there's no need to memoize runningRight since the final results array (see the final loop)
    can be calculated in the same loop, and this guarantees that only the latest runningRight value will be needed
  - Basically: One of the runningTotals must be completely memoized, the other total can use its latest values along
    with the memoized values of the other total to calculate the final array

  Time Complexity: O(N)
  Space Complexity: O(1)
"""


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ln = len(nums)
        res = [1 for _ in range(ln)]
        running_left = nums[0]
        running_right = nums[-1]
        for i in range(1, ln):
            res[i] *= running_left
            res[ln - i - 1] *= running_right
            running_left *= nums[i]
            running_right *= nums[ln - i - 1]
        return res
