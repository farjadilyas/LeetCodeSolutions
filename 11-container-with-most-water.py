"""
  11. Container with the most water
  [ Medium ] | [ ?% ] -- Solved 17/12/2022

  Problem:
  - Given a bar chart
  - Return the two bars that could hold the highest area of water between them

  APPROACH:
  - For a pair of bars, area = min(height[bar1], height[bar2]) x bar2-bar1
  - Naive solution is n^2, working down from there, there is no binary property to this question
  - The only better solution should be linear time
  - Trying a 2 pointer approach, starting with the pointers as far apart as possible since we don't want to cut the
    solution set unnecessarily
  - Pick the first and last bar, calculate area.. the question is: which bar do we rule out?
  - The shortest bar is the obvious answer, for this very good reason: We have already gotten the best result possible
    that will involve the shorter bar. Since the two pointers will get closer together with every iteration, if we
    don't move the shorter bar, we will continue to be limited at least by this shorter bar's height, and we'll be
    decreasing the distance between the selected bar
  - Hence, whenever we select two bars, the area calculated is the best possible result for the shorter bar.
  - So we keep that bar aside, and we move on to the next one and use that pair
  - This logic forms a proof by induction, where we calculate the best possible area for every bar except the tallest
  - The tallest bar's best area has to be = that of the second-tallest bar
  - Hence, moving the pointer at the shorter bar closer to the other side until they overlap, and keeping track of the
    max area encountered will give us the solution

  Time Complexity: O(N)
  Space Complexity: O(1)
"""


def maxArea(self, height: List[int]) -> int:
    first, second = 0, len(height) - 1
    mx = 0
    while second > first:
        mx = max(mx, min(height[first], height[second]) * (second - first))
        if height[second] < height[first]:
            second -= 1
        else:
            first += 1
    return mx
