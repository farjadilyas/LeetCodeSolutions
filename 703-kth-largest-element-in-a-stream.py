"""
  703. Kth Largest Element in a Stream
  [ Easy ] | [ 55.4% ] -- Solved 26/02/2023 -- [ Heap, Data Stream ]

  Problem Statement:
  - Given a starting array that may or may not be empty
  - Guaranteed that nums will be at least of length k-1, so that there will always be k elements to choose from when
    the add() method is called
  - Implement a method add() that consumes a value from a stream and returns the new Kth largest value of the stream
    every time

  Approach:
  - Build and maintain a heap of size k to keep track of the k largest elements, don't need to keep track of other
    elements since there are no removals - so once a top-k element is there, its there until it gets driven out of the
    heap due to enough larger elements
  - The implementation below is relatively complex considering the problem since it takes advantage of heapify and
    heappushpop being faster than heappush followed by heappop

  Time Complexity: O(Nlogk)
  Space Complexity: O(k)
"""

import heapq
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.hp = [nums[i] for i in range(min(len(nums),k))]
        heapq.heapify(self.hp)
        for i in range(k, len(nums)):
            heapq.heappushpop(self.hp, nums[i])

    def add(self, val: int) -> int:
        if len(self.hp) >= self.k:
            heapq.heappushpop(self.hp, val)
        else:
            heapq.heappush(self.hp, val)
        return self.hp[-self.k]
