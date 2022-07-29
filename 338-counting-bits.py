"""
  338. Counting Bits
  [ Easy ] | [ 74.7% ] -- Solved 26/07/2022 -- [ Dynamic Programming, Bit Manipulation ]
  ---------- {{ SUBMISSION STATS }} ---------------
  FASTER THAN: 69.33%
  MEMORY USAGE: 78.9%

  Problem:
  - Given a number n, return an array of length n+1 where each index contains the number of bits in the binary repr
    of the index, like: [0,1,1,2,1,...]

  Approach:
  - IDEA: Write out the first 16-32 answers and see the pattern
  - PATTERN:
    - Define an interval to be the numbers between a power of two
    - The numbers in an interval identical to the numbers in all preceeding intervals + 1

  - Initialize a basic array containing 4 answers
  - Run a loop over the remaining intervals, then run a loop over the preceeding intervals for the current interval,
    append and add one

  Time Complexity: O(N)
  Space Complexity: O(1)
"""

import math


def countBits(self, n):
    """
     Simple implementation, dp array, loop to copy previous intervals
    """
    # Define dp array with some answers
    l = [0, 1, 1, 2]
    if n < 4:
        return l[:n+1]

    # Keep count of the length of dp array before the current interval started being calculated, important since it
    # changes when answers are appended.
    prev_power_len = c_n = 4
    ptr = 0
    while c_n <= n:
        l.append(l[ptr]+1)
        ptr += 1
        c_n += 1
        if ptr == prev_power_len:
            ptr = 0
            prev_power_len *= 2
    return l


def countBits(self, n):
    """
     In this implementation, the interval copying loops are broken into 'clean' and the last remaining loop for
     eliminating some conditional checks. Did not really have an impact on performance
    """
    # Define dp array with some answers
    l = [0, 1, 1, 2]
    if n < 4:
        return l[:n + 1]

    # Get number of loops where the previous intervals will be copied 'cleanly', without interruption
    num_clean_loops = int(math.log2(n))
    prev_power_len = 4
    for i in range(num_clean_loops - 2):
        for j in range(prev_power_len):
            l.append(l[j] + 1)
        prev_power_len *= 2

    # Copy the previous intervals for the last interval which may require incomplete copying
    ptr = 0
    for i in range(n - (2 ** num_clean_loops) + 1):
        l.append(l[ptr] + 1)
        ptr += 1
    return l
