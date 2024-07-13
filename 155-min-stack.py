"""
  155. Min Stack
  [ Medium ] | [ 52.1% ] -- Solved 25/01/2023 -- [ Stack, Design ]

  Problem Statement:
  - Design a stack that supports push, pop, top, and retrieving the minimum element, all in constant time.

  Approach:
  - Take advantage of the fact that the order of deletion is fixed to FIFO
  - Hence, if we know the stack is 0, -2, 3, -3 - then we know the new minimum values if we delete till empty will be
    -3, -2, -2, 0
  - This is the running minimum of the stack - if we save this for each possible deletion step / for each node, we will
    save the minimum for the subset of the stack below it
  - Summary: Store a minimum alongside each node, where the minimum is the minimum value in the subset of the stack
    below (inclusive) the current node
  - This way, getMin will be available in O(1), and will continue to be available in constant time even if we pop from
    the stack
"""

class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append((val, min(val, self.stack[-1][1] if self.stack else 2**31)))

    def pop(self) -> None:
        return self.stack.pop()[0]

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


class MinStackOptimal:
    """
    This MinStack doesn't store a min with every single stack entry
    Instead, it stores a monotonically decreasing min stack with each value that breaks the previous min's record
    - This min_stack also contains the counts of the number of times that min value has been encountered
    - This is required so that if there are multiple elements that are all the min, popping the latest once doesn't
      pop the min stack entry. Instead, we decrement the count var for the min val in the min_stack entry and only
      pop from the min_stack when the count of the min element is zero
    - With this, we only keep the min entries we absolutely need to instead of storing min entries for each stack entry

    Time Complexity of all ops: O(1)
    Space Complexity: O(N) - when input is in decreasing order
    """

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or val < self.min_stack[-1][0]:
            self.min_stack.append([val, 1])
        elif val == self.min_stack[-1][0]:
            self.min_stack[-1][1] += 1

    def pop(self) -> None:
        val = self.stack.pop()
        if val != self.min_stack[-1][0]:
            return
        self.min_stack[-1][1] -= 1
        if self.min_stack[-1][1] == 0:
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1][0]
