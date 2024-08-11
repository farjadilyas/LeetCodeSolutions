"""
  153. Find Minimum in Rotated Sorted Array
  [ Medium ] | [ 48.2% ] -- Solved 31/07/2022 -- [ Array, Binary Search ]
  ----------- {{ SUBMISSION STATS }} --------------
  FASTER THAN: 47.28%
  MEMORY USAGE: 63.23%

  Problem Statement:
  - An array, sorted in ascending order is rotated k times, where each rotation is equivalent to a circular right shift
  - Find the minimum element of the sorted array

  Approach:
  - Have to find the inflection point where nums[ip] < nums[ip-1]

  BINARY SEARCH
  - Advance middle closer to pivot if you're bigger than it, go away from it if you're smaller than it
  - Bound to arrive at inflection point in log n

  Time Complexity: O(log n)
  Space Complexity: O(1)
"""


def findMin(self, nums: list[int]) -> int:
    # If array isn't rotated
    if nums[0] <= nums[-1]:
        return nums[0]

    # Binary search
    start = 0
    end = len(nums) - 1
    middle = (start + end) // 2
    # Check for inflection point
    while nums[middle] > nums[middle - 1]:
        # Compare with pivot to decide direction, want to go towards minimum element
        # Advance closer to pivot if you're bigger than it, go away from it if you're smaller than it
        # Bound to arrive at inflection point in log n
        if nums[middle] > nums[-1]:
            start = middle + 1
        else:
            end = middle - 1
        middle = (start + end) // 2
    return nums[middle]


"""
Solution using bisect template below - super simple to implement - under 3 min
"""


def bisect(low, high, condition):
    while low < high:
        middle = (low + high) // 2
        if condition(middle):
            high = middle
        else:
            low = middle + 1
    return low


class Solution:
    def findMin(self, nums: list[int]) -> int:
        # [3,4,5,1,2] - [F,F,F,T,T] - condition: num <= nums[-1]
        smallest_idx_less_than_pivot = bisect(
            low=0,
            high=len(nums)-1,
            condition=lambda idx: nums[idx] <= nums[-1]
        )
        return nums[smallest_idx_less_than_pivot]
