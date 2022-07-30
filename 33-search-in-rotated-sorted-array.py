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


# Compact code without comments
def search(self, nums, target):
    start = 0
    end = len(nums) - 1
    pivot = nums[-1] + 1
    first = target < pivot

    while True:
        middle = (start + end) // 2
        if nums[middle] == target:
            return middle
        if (nums[middle] > target) == ((nums[middle] < pivot) == first):
            end = middle - 1
        else:
            start = middle + 1
        if end < start:
            return -1


# Commented code
def search(self, nums, target):
    start = 0
    end = len(nums)-1

    # Pivot is defined as the upper bound of the smaller sorted list
    # original list = [s1,s2], rotated = [s2,s1], pivot = s1[-1]+1
    # here, s1 and s2 are both sub-lists that are sorted
    pivot = nums[-1]+1

    # True if target is in s1, not s2 (see above)
    first = target < pivot

    while True:
        middle = int((start+end)/2)
        if nums[middle] == target:
            return middle

        # In normal binary search, we consider the first half if the current middle is too large compared to the target
        # This condition makes the normal binary search move, only if middle is in the same sublist as the target
        # If we are not in the sublist that contains the target, we must move in the opposite direction than the one
        # we'd move in normally to ensure we consider the list that we know may contain the target
        if (nums[middle] > target) == ((nums[middle] < pivot) == first):
            end = middle-1
        else:
            start = middle+1

        # No more elements to consider, so target not found
        if end < start:
            return -1
