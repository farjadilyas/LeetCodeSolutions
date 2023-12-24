"""
  239. Sliding Window Maximum
  [ Hard ] | [ 46.5% ] -- Solved 19/02/2023 -- [ Sliding Window, Hash Table, String ]
  ----------- {{ SUBMISSION STATS }} --------------
  FASTER THAN:75.75%
  MEMORY USAGE: 5.85%

  - Simple sliding window + heap problem
  - TODO: there's probably a better solution out there..
"""


import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        hp = [(-nums[i], i) for i in range(k-1)]
        heapq.heapify(hp)
        res = []
        for i in range(k-1, len(nums)):
            heapq.heappush(hp, (-nums[i], i))
            mn = hp[0]
            while mn[1] <= i-k:
                heapq.heappop(hp)
                mn = hp[0]
            res.append(-mn[0])
        return res