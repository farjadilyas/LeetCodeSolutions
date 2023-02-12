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

def evalRPN(self, tokens: List[str]) -> int:
    stack = []
    for token in tokens:
        if token == '+':
            stack.append(stack.pop() + stack.pop())
        elif token == '-':
            stack.append(-stack.pop() + stack.pop())
        elif token == '*':
            stack.append(stack.pop() * stack.pop())
        elif token == '/':
            second = stack.pop()
            stack.append(int(stack.pop() / second))
        else:
            stack.append(int(token))
    return stack[0]
