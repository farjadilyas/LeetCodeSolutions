"""
  33. Search in Rotated Sorted Array
  [ Medium ] | [ 38.3% ] -- Solved 30/07/2022 -- [ Array, Binary Search ]
  ----------- {{ SUBMISSION STATS }} --------------
  FASTER THAN: 74.797%
  MEMORY USAGE: 91.06%

  Problem Statement:
  - An integer array, sorted in ascending order is rotated such that:
    - original: [s1, s2]
    - rotated: [s2, s1]

  - Write an algorithm that returns the index of a number in the rotated array, and runs in O(log n) time

  APPROACH: SINGLE PASS BINARY SEARCH WITH REVERSE TOGGLE

  - Binary search can help us achieve O(log n) functionality

  ALGORITHM
  - Break problem down into two cases
    - Target number and middle are in the same sublist: In this case, normal binary search works
    - Target number and middle are in the opposite sublist: In this case, normal binary search, with the moves reversed
      - So if middle < target
        - If target and middle are in the same sublist, consider second half
        - Else, consider the first half

  - This algorithm works since if target is in the opposite sublist, then we need to run binary search on the half that
    we KNOW contains target

  IMPORTANT POINT:
  - This algorithm is enabled by the fact that we can know, using one operation, whether target is in s1 or s2 by
    comparing it with the pivot. If target < pivot, it is in the smaller sublist, and vice versa
  - The pivot is defined as the upper bound of the smaller sublist, so pivot = s1[-1]+1
  - Then, all we need to do is in every iteration, find out which sublist middle is in by comparing it to the pivot,
    and reversing the moves if it's in the opposite sublist to the target


  Time Complexity: O(log n)
  Space Complexity: O(1)
"""


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Consider unrotated array to be [s1, s2] where s2 is of length k
        # After k rotations, the array is [s2, s1]
        # We will call s2 the first half and s1 the second half in the code below
        low = 0
        high = len(nums)-1
        is_target_in_first_half = target > nums[-1]
        while low <= high:
            middle = (low + high) // 2
            is_middle_in_first_half = nums[middle] > nums[-1]
            is_middle_in_same_half_as_target = is_middle_in_first_half == is_target_in_first_half
            if nums[middle] == target:
                return middle
            # Consider only the right half of the search space if:
            # - Middle is less than target and is in the same half
            # - Middle is greater than target, but is in the opposite half (think about it with an example)
            if (nums[middle] < target) == is_middle_in_same_half_as_target:
                low = middle + 1
            else:
                high = middle - 1
        return -1
