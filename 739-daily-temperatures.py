"""
  739. Daily Temperatures
  [ Medium ] | [ 66.4% ] -- Solved 02/02/2023 -- [ Array, Stack, Monotonic Stack ]

  Problem Statement:
  - Given an array of integers representing daily temperatures, for each day find the minimum number of days one has
    to wait before a day with a higher temperature occurs
  - Sample Input: [73,74,75,71,69,72,76,73]
  - Sample Output: [1,1,4,2,1,1,0,0]

  Naive Approach O(N^2):
  - For every element, iterate from that point onwards till a higher one is found

  Optimal Approach:
  - It is clear that the goal is to find what position the first larger element occurs at
  - Since a number can only resolve (be the first larger element) elements that occur before it..
    - Iterate over the array, and for each element, attempt to resolve the unresolved ones to its left
    - THE TRICK: is that if you attempt to resolve the most recent element first, and then so on..
    - you will find that the unresolved elements are always decreasing
    - Think of it like this.. you have a decreasing seq [75, 71, 69] and now you encounter 72
    - If you try to resolve the most recent element first, and so on, 72 will resolve the part of the unresolved list
      that conflicted with its decreasing property with the addition of 72
  - Since we attempt to resolve at every step, we're finding the correct minimum num of days
  - Since we resolve it in the correct order, the unresolved list is always decreasing, so we can resolve elements in
    one attempt - no need to search the list
  - Note that elements are added once, and ultimately popped once - no other steps happen - num steps are 2N - O(N)

  - Also note that the stack might be non-empty after the iteration over the array, those are the elements that don't
    have a subsequent day with a higher temperature

  Implementation detail:
  - The manner in which we access the unresolved list is the same as that of a stack - more specifically, this list
    is being used as a monotonic stack
  - In this list, store a tuple (temperature, index of occurrence) - the first helps with the temperature comparison,
    the second allows us to update the desired index in the output array

  Time Complexity: O(N)
  Space Complexity: O(N)
"""


def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    st = []
    for i, temp in enumerate(temperatures):
        while st and st[-1][0] < temp:
            temperatures[st[-1][1]] = i - st[-1][1]
            st.pop()
        st.append((temp, i))
    while st:
        temperatures[st.pop()[1]] = 0
    return temperatures
