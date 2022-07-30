"""
  875. Koko Eating Bananas
  [ Medium ] | [ 53.5% ] -- Solved 31/07/2022 -- [ Array, Binary Search ]
  ----------- {{ SUBMISSION STATS }} --------------
  FASTER THAN:90.32%
  MEMORY USAGE: 97.34%

  Problem Statement:
  - array containing piles of bananas
  - k = rate of bananas consumed per hour
  - can only consume from one pile in an hour
  - find minimum value of k using which all piles can be consumed in h hours

  Approach:
  - given k, can find number of hours required to consume all piles by
    - iterating through array and taking number of times pile divide by k
  - no straightforward way to arrive at min k given h, so we go the other way around and..
  - try different values of k, find the minimum value that requires < h hours for the piles to be consumed

  BINARY SEARCH: Used to find the smallest value of k that satisfies cur_h < h given the range of k
  - k's range is [ceil(piles.sum()/h), max(piles)] - min obtained by assuming piles are optimally (equally) distributed,
    max is obtained by the simple logic that if the eating rate is max(piles), you need one pass to consume all piles,
    minimum h is guaranteed at k=max(piles), which is why it is the max
    - increasing k beyond max(piles) is pointless, since the extra rate won't be used
  - apply binary search on this range of k values, to find the one that satisfies the h constraint and is minimum

  Time Complexity: O(log n)
  Space Complexity: O(1)
"""


import math


def minEatingSpeed(self, piles, h):
    start = end = 0
    for pile in piles:
        if pile > end:
            end = pile
        start += pile
    start = math.ceil(start / h)

    while end > start:
        cur_h = 0
        middle = (start + end) >> 1
        for pile in piles:
            cur_h += math.ceil(pile / middle)
        if cur_h > h:
            start = middle + 1
        else:
            end = middle
    return start
