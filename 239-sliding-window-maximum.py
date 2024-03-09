"""
  239. Sliding Window Maximum
  [ Hard ] | [ 46.5% ] -- Solved 19/02/2023 -- [ Sliding Window, Hash Table, String ]
  ----------- {{ SUBMISSION STATS }} --------------
  FASTER THAN: 79.08%
  MEMORY USAGE: 95.07%

  - Slide a window of a given length over an array and output the maximum element for each step the sliding window takes
  - Clearly a sliding window problem

  - Naive solution is to resort to maintaining the elements inside the sliding window in proper sorted order

  - Better solution makes use of the fact that instead of maintaining full sorted order, we can maintain a
    monotonically decreasing order
  - Explanation: Take the example sliding window [-1, 3, 2]
    - Here, once the sliding window encounters 3, -1 is entirely useless
    - -1 isn't the answer now, and it will never be again since it will go out before the other elements
    - Hence, we learn that as soon as the window encounters 3, the smaller elements to its left can be removed
  - Now it's clear that maintaining a sliding window with monotonically decreasing order will solve this
  - In this case, the window is sliding over, elements are coming in and going out of range

  - So: Slide a monotonically decreasing deque over the array
    - After k-1 steps, start adding the left most element (largest one) of the deque in the answer array

  - Smaller points:
    - Save indices instead of values in the deque, we can get value from index but not the other way round
    - This avoids using extra space for index
"""

from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        ans = [0] * (len(nums)-(k-1))
        for i in range(len(nums)):
            # Pop elements that are smaller than the incoming element
            while queue and nums[i] > nums[queue[-1]]:
                queue.pop()
            queue.append(i)
            # Pop left if left most deque element is k steps behind
            if queue and (i - queue[0]) == k:
                queue.popleft()
            if i >= k-1:
                ans[i-(k-1)] = nums[queue[0]]
        return ans


"""
  Suboptimal solution: Use a heap
  - Maintain a sliding window, all elements in sliding window should be in heap
  - when popping, if the element is out of the window, ignore and pop again
  - this ignores the property where we only need to consider the monotonically decreasing elements of the sliding
    window, and hence don't need to maintain a sorted order
    
  FASTER THAN: 75.75%
  MEMORY USAGE: 5.85%
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