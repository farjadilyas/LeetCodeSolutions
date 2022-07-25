"""
  56. Merge Intervals
  [ Medium ] | [ 45.4% ] -- Solved 26/07/2022 -- [ Arrays, Sorting ]
  ---------- {{ SUBMISSION STATS }} ---------------
  FASTER THAN: 60.70%
  MEMORY USAGE: 84.5%

  Approach:
  - IDEA: Two intervals can be merged by taking the max of the start and min of the end. If end-start is >= 0, the
    intervals overlap
  - Then, the merged interval is the minimum starting time and the maximum ending time

  Problem:
  - If one interval appears that has a smaller starting time than the preceeding intervals, it may not be able to be
    merged properly with the preceeding intervals in one pass since some intervals that were thought of as ones that
    can't be merged have already been added to the output array
  - A simple solution for this is to sort the input array based on the starting times, ensuring that no odd-one-out
    inputs are received when answers that didn't consider them have already been outputted

  - HENCE, we arrive at the optimal solution that involves sorting and one pass for merging

  Time Complexity: O(NlogN)
  Space Complexity: O(1) -- depends on sorting algorithm
"""


def merge(self, intervals):
    intervals = sorted(intervals, key=lambda x: x[0])
    prev = intervals[0]
    out = [prev]
    for interval in intervals:
        if interval[1] < prev[1]:
            o_end = interval[1]
            end = prev[1]
        else:
            o_end = prev[1]
            end = interval[1]

        if interval[0] > prev[0]:
            o_start = interval[0]
            start = prev[0]
        else:
            o_start = prev[0]
            start = interval[0]

        if o_end - o_start >= 0:
            prev = out[-1] = [start, end]
        else:
            out.append(interval)
            prev = interval
    return out
