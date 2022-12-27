"""
  268. Missing Number
  [ Easy ] | [ ?% ] -- Solved 25/12/2022

  Problem:
  - Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range
    that is missing from the array.

  APPROACH:
  - Whenever we need to find a missing number, XOR is a clear possible solution since it cancels out the same numbers,
    regardless of the order they appear in
  - We expected numbers in the range of [0, n], but one is going to be missing
  - 0 doesn't have an effect on XOR, so if we could XOR the entire array with the range [1, n], the result would be the
    missing number
  - Just iterate through the array, running_xor = running_xor ^ (index + 1) ^ nums[index]

  Time Complexity: O(N)
  Space Complexity: O(1)
"""


def missingNumber(self, nums: List[int]) -> int:
    missing_num = 0
    for i in range(len(nums)):
        missing_num = missing_num ^ (i + 1) ^ nums[i]
    return missing_num