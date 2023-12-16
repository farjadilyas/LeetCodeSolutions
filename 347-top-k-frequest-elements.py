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


"""
    Quickselect approach
    - Build freq dist of nums, need to sort the unique keys based on their frequencies
    - Alter quickselect partition to compare using frequencies instead of values themselves
"""
from collections import Counter
import random


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        unique = list(count.keys())

        def partition(left, right, pivot_index):
            pivot_frequency = count[unique[pivot_index]]

            # Move pivot to the end
            unique[right], unique[pivot_index] = unique[pivot_index], unique[right]

            store_index = left
            for i in range(left, right):
                # If the element encountered is less than the pivot
                # swap it with the first unswapped element that is greater than the pivot
                if count[unique[i]] < pivot_frequency:
                    unique[store_index], unique[i] = unique[i], unique[store_index]
                    # Move store_index+1, +1 is guaranteed to give an element that is supposed to be in
                    # the greater partition, because if there were elements that were supposed to be in the left,
                    # they would have been swapped with store index
                    store_index += 1
            # At the end of the loop, store_index will mark the beginning of the greater subarray
            unique[right], unique[store_index] = unique[store_index], unique[right]
            # store_index now marks the correct index of the pivot in the final array
            return store_index

        def quickselect(left, right, k_smallest):
            if left == right:
                return

            pivot_index = random.randint(left, right)
            pivot_index = partition(left, right, pivot_index)
            # eg: 6 smallest, pivot works for us if its at index 6, meaning the 6 smallest elements are at 0-5
            if k_smallest == pivot_index:
                return
            # we picked too many elements in the smallest array, pick another pivot
            elif k_smallest < pivot_index:
                quickselect(left, pivot_index - 1, k_smallest)
            else:
                quickselect(pivot_index + 1, right, k_smallest)

        n = len(unique)
        # k function param is k largest, n-k gives ksmallest
        quickselect(0, n - 1, n - k)
        return unique[n - k:]
