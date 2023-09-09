"""
  57. Insert Intervals
  [ Medium ] | [ 39.3% ] -- Solved 11/07/2023 -- [ Arrays ]
  ---------- {{ SUBMISSION STATS }} ---------------
  FASTER THAN: 99.35%
  MEMORY USAGE: 97.85%

  Approach:
  - The input is already sorted by starting date, and all intervals in it are non-overlapping
  - So iterate through the intervals and find the point where this new interval will be inserted
  - Iterate to the left and right and extend the window of intervals the new interval overlaps with
  - Replace those intervals with these

  Time Complexity: O(N)
  Space Complexity: O(1)
"""


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        idx = 0
        for interval in intervals:
            if interval[0] > newInterval[0]:
                break
            idx += 1

        lidx = idx - 1
        min_start = newInterval[0]
        while lidx >= 0 and newInterval[0] <= intervals[lidx][1]:
            if intervals[lidx][0] < min_start:
                min_start = intervals[lidx][0]
            lidx -= 1

        ridx = idx
        max_end = max(intervals[idx - 1][1], newInterval[1]) if idx - 1 >= 0 else newInterval[1]
        while ridx < len(intervals) and newInterval[1] >= intervals[ridx][0]:
            if intervals[ridx][1] > max_end:
                max_end = intervals[ridx][1]
            ridx += 1

        # print(lidx, ridx)
        del intervals[lidx + 1: ridx]
        intervals.insert(lidx + 1, [min_start, max_end])
        return intervals
