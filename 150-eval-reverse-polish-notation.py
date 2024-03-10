"""
  150. Evaluate Reverse Polish Notation
  [ Medium ] | [ 45.2% ] -- Solved 25/01/2023 -- [ Array, Math, Stack ]

  Problem Statement:
  - Given a list of tokens representing a mathematical expression in postfix, evaluate it

  Approach:
  - In postfix notation, read the expression left-to-right, any operator operates on the two operands right before it
  - The answer should replace all tokens used up in the evaluation in-place, and will in-turn be used down the line
    as an operand
  - Use a stack to store operand as they're encountered. When an operator is met, pop 2 operands, apply the operator
    on them and replace them

  Time Complexity: O(N)
  Space Complexity: O(N)
"""


class Solution:
    def __init__(self):
        self.op_map = {
            '+': lambda y, x: x + y,
            '-': lambda y, x: x - y,
            '*': lambda y, x: x * y,
            '/': lambda y, x: int(x / y)
        }

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            stack.append(self.op_map[token](stack.pop(), stack.pop()) if token in self.op_map else int(token))
        return stack[0]
