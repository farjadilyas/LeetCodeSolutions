"""
  919. Meeting Rooms II
  [ Medium ] | [ 39.3% ] -- Solved 11/07/2023 -- [ Arrays ]
  ---------- {{ SUBMISSION STATS }} ---------------
  FASTER THAN: 99.35%
  MEMORY USAGE: 97.85%

  Approach:
  -

  Time Complexity: O(N)
  Space Complexity: O(1)
"""


from typing import (
    List,
)
from lintcode import (
    Interval,
)

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

import heapq

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def min_meeting_rooms(self, intervals: List[Interval]) -> int:
        sorted()
        if not intervals: return 0
        intervals.sort(key=lambda e: e.start)
        hp = [intervals[0].end]
        for idx in range(1, len(intervals)):
            if hp[0] <= intervals[idx].start:
                heapq.heappushpop(hp, intervals[idx].end)
            else:
                heapq.heappush(hp, intervals[idx].end)
        return len(hp)

