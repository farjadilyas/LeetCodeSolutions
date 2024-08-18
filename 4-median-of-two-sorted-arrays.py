"""
  4. Median of Two Sorted Arrays

  Key Intuition:
  - It's clear we want to run binary search to find 2 points that partition the input into two equal halves to achieve
    the target log(m+n) time complexity
  - If you run binary search on one array, you don't need to run it on the other since we know the number of elements
    to be expected in the left half. So if you pick 2 from one, half=6, then other partition will have first 4 elements
  - What constitutes a valid partition?
    - Let's say after partitioning nums1 = [n1_lhs, n1_rhs] and nums2 = [n2_lhs, n2_rhs]
    - n1_rhs and n2_rhs must be greater than n1_lhs and n2_lhs
    - n1_rhs is obviously greater than n1_lhs due to sorting
    - so the validity condition is: n2_rhs >= n1_lhs and n1_rhs >= n2_lhs

  Approach:
  - The nature of the problem is that we want to find an exact match - use the exact match template
  - There are many edge cases mainly when we pick zero elements from an array
  - SIMPLIFYING EDGE CASES:
    - Use sensible defaults for the values we'll use to compare partitions so that we don't repeatedly, awkwardly check
      whether something is in bounds
    - We are guaranteed to find a median, use a ``while True`` loop rather than ``start <= end``, especially since
      picking zero elements from an array is a legit case
"""


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums2) > len(nums1):
            nums2, nums1 = nums1, nums2
        N1_LEN, N2_LEN = len(nums1), len(nums2)
        N = N1_LEN + N2_LEN
        target_left_half_size = N // 2
        start, end = 0, len(nums2)-1
        NEG_INF, INF = float("-inf"), float("inf")
        while True:
            nums2_idx = (start + end) // 2
            target_num_from_nums1 = target_left_half_size - (nums2_idx + 1)
            nums1_idx = target_num_from_nums1 - 1

            # when comparing that this lhs partition is less than the other rhs partition
            # we want the result to be True if this partition is empty
            # which is why -inf works as the lhs value for empty partitions
            nums1_l = nums1[nums1_idx] if nums1_idx >= 0 else NEG_INF
            nums2_l = nums2[nums2_idx] if nums2_idx >= 0 else NEG_INF
            # when checking that the rhs partition is greater than the other lhs partition
            # we want the result to be True by default if this partition is empty
            # which is why inf works as the rhs value for empty partitions
            nums1_r = nums1[nums1_idx+1] if nums1_idx+1 < N1_LEN else INF
            nums2_r = nums2[nums2_idx+1] if nums2_idx+1 < N2_LEN else INF

            if nums2_r < nums1_l:
                # n2 rhs has smaller elements than n1 lhs, increase n2 elements
                start = nums2_idx + 1
            elif nums1_r < nums2_l:
                # n1 rhs has smaller elements than n2 lhs, decrease n2 elements
                end = nums2_idx - 1
            else:
                # correct partition
                if N % 2:
                    # odd - [1,2,3,4,5] - 3 in rhs - min of rhs partitions
                    return min(nums1_r, nums2_r)
                else:
                    # even - [1,2,3,4] - 2,3 - (max(lhs partitions) + min(right parts)) / 2
                    return (max(nums1_l, nums2_l) + min(nums1_r, nums2_r)) / 2
