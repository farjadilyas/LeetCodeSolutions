"""
  53. Maximum Subarray
  [ Medium ] | [ 49.7% ] -- Solved 24/04/2022 -- [ DP, Arrays, Divide & Conquer ]

  Problem:
  - Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum
    and return its sum.

  Approach:
  - Think of an interval as the starting point for the current subarray being considered as the maximum subarray
  - Keep a running total corresponding to the current interval
  - If the running total dips below 0, then restarting the interval is always going to give a more optimal result, or
    else you'll be starting from below 0...
  - Loop, apply these rules, remember the peak of the running total, this is the sum of the maximum subarray

  Time Complexity: O(N)
  Space Complexity: O(1)
"""


def maxSubArray(self, nums):
    started = False
    all_negative = True
    max_elem = -(10 ** 4) - 1
    running_total = 0
    true_max_running_total = 0

    for idx, elem in enumerate(nums):
        if all_negative:
            max_elem = max(elem, max_elem)
            if max_elem > 0:
                all_negative = False
        if not started and elem >= 0:
            started = True
            running_total = elem
        elif running_total + elem > 0:
            running_total += elem
        else:
            running_total = 0
            started = False
        true_max_running_total = max(running_total, true_max_running_total)

    return max_elem if true_max_running_total == 0 else true_max_running_total


"""
  Much simpler code for the same logic, instead of multiple if conditions, can use max() to decide between continuing
  existing interval or starting a new one.
  
  In the previous implementation, resetting the running total to zero introduced the need for handling the all negative
  case explicitly. Here, instead of resetting the running total to zero, it is set to the current num. The surrounding
  logic supports that.
"""


def maxSubArray(self, nums):
    global_max = local_max = nums[0]
    for num in nums:
        # Max between starting a new interval here or continuing the current interval
        local_max = max(local_max, num + local_max)
        global_max = max(global_max, local_max)
    return global_max
