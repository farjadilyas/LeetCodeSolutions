"""
  437. Top K Frequent Elements
  [ Medium ] | [ 64.8% ] -- Solved 25/07/2022
  ----------- {{ SUBMISSION STATS }} --------------
  FASTER THAN: 99.27%
  MEMORY USAGE: 71.68%

  Problem:
  - Given an integer array nums and an integer k, return the k most frequent elements
  - You may return the answer in any order.

  Approach:
  - Need to index integers quickly to alter their count - can use a hashmap for that
  - Once we have built the correct frequency distribution, the fastest way to get the k largest elements is
    sorting / using a heap
  - NOTE: Sorting is slower than heapify+heappop, since heapify is linear, and heappop is logN*K, and K must be less
    than N - confirmed via submissions

  Time Complexity: O(N + KlogN)
    -> Building frequency dist: O(N)
    -> Building heap: O(N)
    -> Getting K max elem from heap: O(KlogN)
  Space Complexity: O(N)
"""
import heapq
def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    hm = {}
    for num in nums:
        if num in hm:
            hm[num][0] += 1
        else:
            hm[num] = [0, num]
    hp = list(hm.values())
    heapq._heapify_max(hp)
    return [heapq._heappop_max(hp)[1] for _ in range(k)]

    # Sorting alternative - slower
    # hp = sorted(hm.values(), key=lambda x: x[0], reverse=True)
    # return [i[1] for i in hp[:k]]

