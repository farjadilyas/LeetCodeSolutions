"""
  919. Meeting Rooms II
  [ Hard ] | [ 48.7% ] -- Solved 27/08/2023 -- [ Array, Binary Search, Line Sweep, Sorting, Heap ]
  ---------- {{ SUBMISSION STATS }} ---------------
  FASTER THAN: 60.99%
  MEMORY USAGE: 5.06%

  Approach:
  - Solution is a line-sweep algorithm, draw out the intervals
  - Instead of considering just the start and end points of intervals as we usually do in line sweep algorithms, we
    will also consider the query points

  - Sort the start, end and query points, place the 3 pointers at the start and pick the smallest
    (priority: start, query, end) since ends are inclusive
  - Start point: Add (interval length, interval end) to priority queue
  - Query point: Get minimum interval from priority queue
  - End point: Remove all intervals ending at that point
    - IMPORTANT: This is the tricky part
    - so we will make the typical simplification and do a lazy delete on the heap if the minimum element ended before
      the current query
    - (This also means that we don't have to maintain the query pointer and sorted array)

  - Summary: Go over the interval AND query in sorted order, maintain a heap of the intervals that are in contention
    for the smallest interval at a point
  - Sorted order means that we can be confident we are considering all and only the intervals we need to

  Time Complexity: O(NlogN) - sorting, and heap push and pop
  Space Complexity: O(NlogN) - heap
"""


import heapq
import numpy as np


class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # Sort intervals (effective by starting time) so that upon querying we know we are considering the right ones
        intervals.sort()
        # Need to query in ascending order, allows us to do it in one pass
        qargs = np.argsort(queries)
        # Heap value format: (interval_length, interval_end_value)
        # Min-heap by interval length, allows us to use the end value for lazy deletion of out of scope intervals
        hp = []
        qidx = sidx = 0
        li, lq = len(intervals), len(queries)
        while qidx < lq:
            true_qidx = qargs[qidx]
            # Consider any intervals starting in time for the next query
            if sidx < li and intervals[sidx][0] <= queries[true_qidx]:
                heapq.heappush(hp, (intervals[sidx][1]-intervals[sidx][0]+1, intervals[sidx][1]))
                sidx += 1
            else:
                # Lazily delete intervals that have ended before this query
                while hp and hp[0][1] < queries[true_qidx]:
                    heapq.heappop(hp)
                # Get the smallest interval that covers this query
                queries[true_qidx] = hp[0][0] if hp else -1
                qidx += 1
        return queries
