"""
  [ INTERVIEW QUESTION ]
  532. K-Diff Pairs in an Array
  [ Medium ] [ 40.3% ] -- Solved 24/06/2022 -- [ HashMap ]
  ----------------------------------------

  Find distinct pairs in array (a, b) such that a+k = b, k is given
  a and b cannot be picked from the same index, this was not the case in the interview question I got

  Approach:
  - If you want to do it in O(N) time, need a way to lookup whether a number is available to pair in constant time
  - Use a hashmap for that
  - General solution is to use two iterations, one to fill hashmap, other to iterate over array and look k steps to the left
    and right of the number in the hashmap, and remove the item from the hashmap once its been paired twice

  - The solution below is a one iteration solution, where the status of the number is kept track of using integers. The
    following scheme is used:
        - 0: Not paired, 1: Paired smaller number (e-k), 2: Paired with larger number (a+k), 3: Paired with two distinct
          numbers and is not available to pair
        - This scheme is useful since setting the state is cheap using the logical OR operator '|'
        - Plus, in a-k and the a+k conditions, we can set the values by setting the left and right bits to one respectively
        - Once both bits are set, the number is 3, and is considered as paired

  - EDGE CASE: When k=0, the above logic pairs the number with itself. That is handled in a special case where if k=0,
    the number is inserted, when it is encountered again, it is explicitly set to 3

  Time Complexity: O(N)
  Space Complexity; O(N)
"""

from collections import Counter

# LeetCode 532 Version
def findPairs(self, nums: List[int], k: int) -> int:
    hm = Counter(nums)
    if k == 0:
        return sum(v > 1 for v in hm.values())
    return sum(e + k in hm for e in hm)


# Variant found in interview, where a and b don't have to be distinct elements in the array
def findPairs(arr, k):
    count = 0
    hm = {}
    for e in arr:
        if e not in hm:
            hm[e] = 0
        elif hm[e] == 3:
            continue
        if e-k in hm and hm[e-k] < 3:
            hm[e] = hm[e] | 1
            hm[e-k] = hm[e-k] | 2
            count += 1
        if e+k in hm and hm[e+k] < 3:
            hm[e] = hm[e] | 2
            hm[e + k] = hm[e + k] | 1
            count += 1
    return count