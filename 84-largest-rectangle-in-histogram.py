"""
    84. Largest Rectangle in Histogram
    [ Hard ] | [ 39.3% ] -- Solved 04/11/2023 -- [ Array, Monotonic Stack ]
    ---------- {{ SUBMISSION STATS }} ---------------
    FASTER THAN: 98.53%
    MEMORY USAGE: 83.98%
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
        # 1 1 1 1 1 4 1
        # 1 1 1 1 1 4 4
        # 1 1 1 1 1 2 2 4
        stack = [(heights[0], 0)]
        heights.append(0)
        mx = heights[0]
        for i in range(1, len(heights)):
            height = heights[i]
            if height > stack[-1][0]:
                stack.append((height, i))
            elif height < stack[-1][0]:
                while stack and height < stack[-1][0]:
                    peak_height, peak_index = stack.pop()
                    mx = max(mx, peak_height * (i - peak_index))
                stack.append((height, peak_index))
        return mx
