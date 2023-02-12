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
