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

def productExceptSelf(self, nums: List[int]) -> List[int]:
    l = len(nums)
    res = [0 for _ in range(l)]
    res[0] = nums[0]
    for i in range(1, l):
        res[i] = res[i - 1] * nums[i]
    rev_run = 1
    for i in range(l - 1, 0, -1):
        res[i] = res[i - 1] * rev_run
        rev_run *= nums[i]
    res[0] = rev_run
    return res
