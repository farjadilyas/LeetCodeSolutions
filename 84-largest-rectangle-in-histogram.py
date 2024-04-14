"""
    84. Largest Rectangle in Histogram
    [ Hard ] | [ 39.3% ] -- Solved 04/11/2023 -- [ Array, Monotonic Stack ]
    ---------- {{ SUBMISSION STATS }} ---------------
    FASTER THAN: 98.53%
    MEMORY USAGE: 83.98%

    INTUITION:
      - This problem uses the 'Previous Smaller Element' as a subproblem
      - Every candidate rectangle is limited by the height of one bar
      - For each bar, calculate its maximal rectangle (the rectangle whose height this bar limits)
        by looking to its left and right
      - To get the left bound of the rectangle, you need the previous smaller element
      - To get the right bound, you need the next smaller element
      - The sub-problem is solved using a monotonic stack
      - The optimal solution below (described below) simply removes the need for the right run by a clever change..
        - Notice that in the previous smaller element solution, a stack entry is popped when a smaller element than it is
          encountered
        - This newly encountered element is, in fact, the answer for the next smaller element!
        - So we can just implement the solution for the previous smaller element, and when popping from the stack we also
          understand the next smaller element. Hence, the maximal rectangle for the element being popped is calculated!
        - We can add append a dummy zero entry in the histogram to force all calculations to be completed

    APPROACH:
    Maintain an increasing monotonic stack - each element of this stack represents running totals that are still being explored
    - stack entries are in the following format: (height, starting index of the running total)

    Iterate over the heights, left to right, with the following rules:
    - If the new height is higher than the previous one
        - It can potentially support a higher total, eg: (5, 6, 6, 6)
        - So add it as a new entry in the stack with the current index since it is a promising new running total
    - If the new height is less than the previous one..
        - All running totals with max heights that are higher than this new height will now be limited to this height
        - Remove such running totals, calculate the largest rectangle they enable, UPDATE THE MAX WITH THIS, before removing them - these running totals have reached their potential
        - Add a new stack entry for the adjusted running total (limited by the current height), but IMP: the starting index of this running total will be the starting index of the earliest running ttoal that was removed in this step (eg: [1,5,6] running totals, 2 is the new entry, 5 and 6 running totals are removed, and the running total with height=2 starts from the index of 5, not the current index)

    - Finally, at the end of the iteration, there may be running totals that have not been concluded, an easy way to handle this is to add a dummy 0 entry at the end of the heights array
    - This will effectively end all running totals, so they'll be taken into consideration
"""


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        heights.append(0)
        max_area = 0
        for i in range(len(heights)):
            running_start = i
            while stack and stack[-1][0] > heights[i]:
                running_height, running_start = stack.pop()
                max_area = max(max_area, running_height * (i - running_start))
            stack.append((heights[i], running_start))
        return max_area


# TODO: implement the divide and conquer approach
# TODO: check out the segment tree approach


"""
  For the recursive approach - a note on the complexity analysis:
  - Average case (minimum in the middle):
     - First level goes through N elements to search for minimum
     - Second level goes through a total of N-1 elements
     - Third level goes through a total of N-3 elements (draw it out)
     
     - sequence is like: N, N-1, N-3, N-7..
     - change it to (N, N-2, N-4, N-8...) + logN - 1
     - sequence has logN elements
     - N part becomes NlogN
     - 0, -2, -4.. part becomes -(2^(log(N)-1)) --> -(N-1)
     - overall formula is: Nlog(N) - (N - 1) + (logN - 1)
         - final: Nlog(N) + log(N) - N ----> O(Nlog(N))
  - Worst case (if input is sorted)
    - Sequence in this case is N, N-1, N-2
    - or 1,2,3,..,N --> N(N-1)/2 ----> O(N^2)
"""
