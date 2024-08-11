"""
  875. Koko Eating Bananas
  [ Medium ] | [ 53.5% ] -- Solved 12/02/2023 -- [ Array, Binary Search ]
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


from math import ceil


def minEatingSpeed(self, piles, h):
    """
    Old solution without a bisect template - tougher to handle edge cases
    """
    start = end = 0
    for pile in piles:
        if pile > end:
            end = pile
        start += pile
    start = ceil(start / h)

    while end > start:
        cur_h = 0
        middle = (start + end) >> 1
        for pile in piles:
            cur_h += ceil(pile / middle)
        if cur_h > h:
            start = middle + 1
        else:
            end = middle
    return start


"""
  Below, we use a bisect template that works well for all binary search problems
  
  Because all of these problems can be modelled as find the smallest idx that satisfies X condition
"""


def bisect(low, high, condition):
    """
    First the smallest idx in [low, high] for which ``condition`` returns ``True``
    """
    while low < high:
        middle = (low + high) // 2
        if condition(middle):
            high = middle
        else:
            low = middle + 1
    return low


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        return bisect(
            low=ceil(sum(piles)/h),
            high=max(piles),
            condition=lambda k: sum(ceil(pile/k) for pile in piles) <= h
        )
