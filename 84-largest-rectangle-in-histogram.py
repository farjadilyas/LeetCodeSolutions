"""
    84. Largest Rectangle in Histogram
    [ Hard ] | [ 39.3% ] -- Solved 04/11/2023 -- [ Array, Monotonic Stack ]
    ---------- {{ SUBMISSION STATS }} ---------------
    FASTER THAN: 98.53%
    MEMORY USAGE: 96.68%

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
from typing import List, Callable, Any


class OptimalSolution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        heights.append(0)
        max_area = 0
        for i in range(len(heights)):
            running_start = i
            while stack and stack[-1][0] >= heights[i]:
                running_height, running_start = stack.pop()
                max_area = max(max_area, running_height * (i - running_start))
            stack.append((heights[i], running_start))
        return max_area


class BruteForceSolution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        Slightly better than the actual brute force which calculates the minimum inside the nested loop
        """
        max_area = 0
        for i in range(len(heights)):
            min_h = 1_000_000
            for j in range(i, len(heights)):
                min_h = min(min_h, heights[j])
                max_area = max(max_area, (j-i+1) * min_h)
        return max_area


class DivideAndConquerSolution:
    """
      For the recursive approach - a note on the complexity analysis:
      - Average case (minimum in the middle):
         - First level goes through N elements to search for minimum
         - Second level goes through a total of N-1 elements
         - Third level goes through a total of N-3 elements (draw it out)

         - sequence is like: N, N-1, N-3, N-7..
         - sequence has logN elements on avg, so N part becomes NlogN
         - the -1, -3, -7 parts will always add up to N (since these are the min bars being taken out of consideration)
         - overall formula is: Nlog(N) - N
      - Worst case (if input is sorted)
        - Sequence in this case is N, N-1, N-2
        - or 1,2,3,..,N --> N(N-1)/2 ----> O(N^2)
    """
    def largestRectangleArea(self, heights: List[int]) -> int:
        def recurse(start, end):
            if start >= end:
                return 0
            min_idx = min(range(start, end), key=lambda e: heights[e])
            return max(
                (end-start) * heights[min_idx],
                recurse(start, min_idx),
                recurse(min_idx+1, end)
            )
        return recurse(0, len(heights))


class SegmentTreeSolution:
    """
    This solution is almost exactly the same as the Divide and Conquer solution, but with one improvement
    It uses segment trees to find the minimum in log(N) instead of N.

    Worst case time complexity is O(Nlog(N)) - N part is when array is sorted, so we don't have balanced sub-problems
    Average case time complexity is N (logN for the recursion depth, and logN for each step)
    Space Complexity: O(N)
    """
    def largestRectangleArea(self, heights: List[int]) -> int:
        # We want the index of the minimum height in an index range
        # Send an array of indices
        # The aggregation to be done is: get index with the smaller height
        # So each node of the segment tree will store the index with the min height for its segment
        segment_tree = SegmentTree(
            nums=list(range(len(heights))),
            operation=lambda x, y: x if heights[x] < heights[y] else y
        )

        def recurse(start, end):
            if start >= end:
                return 0
            min_idx = segment_tree.aggregate(start, end - 1)
            return max(
                (end - start) * heights[min_idx],
                recurse(start, min_idx),
                recurse(min_idx + 1, end)
            )
        return recurse(0, len(heights))


# TODO: Move segment tree implementation to some sort of utils
# TODO: implement update function


from math import log, ceil, pow


class SegmentTree:
    """
    My general-purpose segment tree implementation.

    Tree with input array of size N as leaf nodes, and the tree aggregating 2 nodes at a time all the way to the root.
    The aggregation can be specified via the ``operation`` param. Number of nodes = 2 * (next pow of 2 after N) - 1

    Construction: O(N) DFS
    Searching segment: O(log(N))
    Updating value (leaf-node): O(log(N))
    """

    def __init__(self, nums: list[int], operation: Callable[[Any, Any], Any]):
        self.nums = nums
        len_nums = len(nums)
        # To represent a tree with N elements, you need an array of the size 2*(next pow of 2 that is >= N) - 1
        self.next_power_of_two = len_nums if (len_nums & (len_nums - 1)) == 0 else pow(2, ceil(log(len_nums, 2)))
        self.tree = [None] * int((2 * self.next_power_of_two) - 1)
        self.operation = operation
        self.construct(0, len(self.nums) - 1, 0)

    def construct(self, low, high, pos):
        """
        DFS that goes down an uninitialized segment tree, hydrates the leaf node values from ``nums``, then while
        backtracking aggregates from the leaves up to the root

        We're maintaining the following 2 sets of data

        - [low, high] - Tells us the segment this node will store the result for, necessary to recognize leaf nodes
          and know where to pick data from for each leaf node
        - pos: This tracks the index of the tree array that corresponds to the node in the recursion tree we're
          currently at, eg pos=1 is root.left
        """
        # Leaf-node values should be copied straight from the input array
        if low == high:
            self.tree[pos] = self.nums[low]
            return
        # 'Aggregate' values higher up should be combined from the next level child values
        mid = (low + high) // 2
        left_child_idx, right_child_idx = (2 * pos) + 1, (2 * pos) + 2
        self.construct(low, mid, left_child_idx)
        self.construct(mid + 1, high, right_child_idx)
        self.tree[pos] = self.operation(self.tree[left_child_idx], self.tree[right_child_idx])

    def aggregate(self, target_start, target_end):
        def aggregate_helper(start, end, pos):
            # No overlap - we're returning None here since in case of getting min index, there's no good default
            # Otherwise, you could return a large value when using this segment tree for mininums for eg
            if target_start > end or target_end < start:
                return None

            # Complete overlap: If [start, end] is entirely inside [target_start, target_end],
            # then this node is a segment that is part of the answer
            if target_start <= start and end <= target_end:
                return self.tree[pos]
            else:
                # Partial overlap
                middle = (start + end) // 2
                left_aggregate = aggregate_helper(start, middle, (2 * pos) + 1)
                right_aggregate = aggregate_helper(middle + 1, end, (2 * pos) + 2)
                if left_aggregate is None or right_aggregate is None:
                    return left_aggregate if right_aggregate is None else right_aggregate
                return self.operation(left_aggregate, right_aggregate)

        return aggregate_helper(0, len(self.nums) - 1, 0)


# Testing summation using Segment Trees
input = [2, 4, -1, 3, -6, 7, 1, 10]
st = SegmentTree(nums=input, operation=lambda x, y: x + y)
print(st.tree)
assert all(st.aggregate(0, i) == sum(input[:i + 1]) for i in range(len(input)))
print(st.aggregate(0, 3))




