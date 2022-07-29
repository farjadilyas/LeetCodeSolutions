"""
  287. Find the Duplicate Number
  [ Medium ] | [ 59.0% ] -- Solved 26/07/2022 -- [ Array, Two Pointers ]

  Problem Statement:
  - An array of n+1 integers, each of which is in the range [1, n]
  - There is only one repeated number, find it
  - Using only constant space
"""


"""
  APPROACH #1: BINARY SEARCH
  - Sort the array, so the duplicates occur together
  - Since the integers are in range [1,n] and there are n integers, we can make the following assumption:
    - If the left part of the array, that has been read, does not contain a duplicate, then arr[n] = n+1
    - Hence, if arr[n] is smaller than expected, the duplicate is to the left
    - If arr[n] is larger than expected, the duplicate is to the right
  
  - Hence, it is sort + binary search to narrow down on the duplicated element
  
  Time Complexity: O(NlogN)
  Space Complexity: O(1) - depends on sorting algorithm
"""


def findDuplicate(self, nums):
    nums.sort()
    start = 0
    end = len(nums)-1
    while True:
        if end <= start:
            return nums[start]
        middle = int((start+end)/2)
        if nums[middle] >= middle+1:
            start = middle+1
        else:
            end = middle-1


"""
  APPROACH #2: FLOYD'S CYCLE FINDING ALGORITHM - FAST AND SLOW
  - Interpret the input array as a linked list, where the indices are the nodes, and the values are the pointers
  - This means that duplicate values -> multiple pointers to the same node -> a cycle
  
  - Use Floyd's cycle finding algorithm, fast and slow pointer, remember where the intersect
  - Reset the slow pointer, run the slow and fast pointers at the same speed now
  - The node of intersection is now the node where the cycle starts
  
  Time Complexity: O(N) - Floyd's Cycle finding algorithm provably completes in linear time
  Space complexity: O(1)
"""


def findDuplicate(self, nums):
    # Initialize slow and fast variables
    # Let them be a bit ahead of their original starting position so the
    # Not equal condition works on the first iteration
    slow = nums[nums[0]]
    fast = nums[slow]
    while slow != fast:
        slow = nums[slow]
        fast = nums[nums[fast]]

    # Reset slow to the start
    # Step both at the same rate forward, they'll meet at the start of the loop
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    return slow
