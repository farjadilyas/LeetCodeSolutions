"""
  295. Find Median from Data Stream
  [ Hard ] | [ 51.4% ] -- Solved 20/03/2023 -- [ Heap, Data Stream, Two Pointers, Sorting ]

  Problem Statement:
  - the title

  Approach:
  - Its obvious that we need to maintain sorted order since its a stream, so new data can fit in anywhere
  - Naive way to do this to maintain a sorted array, and just index the middle for findMedian
  - We know heaps are useful for maintaining sorted order in a scenario where insertions can happen anywhere in the
    sorted sequence
  - But we need to find the middle most value of the heap
  - Easy way to do this is to maintain two heaps, on either side of the median value
  - In order to handle the case of odd/even values, we can decide that the greater heap will be equal to, or 1 greater
    than the smaller heap in size
  - Hence, if the number of elements are odd, the min of the minHeap is the answer, if they're even, then the avg of the
    maxHeap's max and the minHeap's min is the answer

  Insertion strategy:
  - Compare the incoming value to the maxHeap's max to find out which heap it belongs to
  - Insert it into that heap
  - If the heap where the insertion has just happened is now breaking its size constraint relative to the other heap,
    re-balance it by moving an element to the other heap. Examples are:
    - If the maxHeap is too big, move the maxHeap's max to the minHeap, and vice versa
    - This works very well since the element that should be shifted first is always available at the root, so
      re-balancing is O(logN), just like insertion

  Time Complexity: O(NlogN)
  Space Complexity: O(N)
"""


import heapq
class MedianFinder:

    def __init__(self):
        self.maxHeap = []
        self.minHeap = []

    def addNum(self, num: int) -> None:
        # If element belongs in first half, add it, if the first half is too big now, shift its biggest elem to the 2nd
        if self.maxHeap and num < -self.maxHeap[0]:
            heapq.heappush(self.maxHeap, -num)
            if len(self.maxHeap) > len(self.minHeap):
                heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))
        else:
            # If the element belongs in the 2nd half, add it, and if this gets too big, shift the smallest to 1st half
            heapq.heappush(self.minHeap, num)
            if len(self.minHeap) - len(self.maxHeap) > 1:
                heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))

    def findMedian(self) -> float:
        return self.minHeap[0] if (len(self.maxHeap) + len(self.minHeap))%2 else (self.minHeap[0] -self.maxHeap[0])/2