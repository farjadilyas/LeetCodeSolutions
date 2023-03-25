"""
  703. Kth Largest Element in a Stream
  [ Easy ] | [ 64.8% ] -- Solved 26/02/2023 -- [ Heap, Array ]

  Problem Statement & Approach: Easy

  Time Complexity: O(NlogN)
  Space Complexity: O(N)
"""

import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -stones[i]
        heapq.heapify(stones)
        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if first != second:
                heapq.heappush(stones, first-second)
        return -stones[0] if stones else 0
