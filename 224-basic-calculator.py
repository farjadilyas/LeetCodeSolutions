"""
  224. Basic Calculator
  [ Hard ] | [ 43.7% ] -- Solved 14/07/2024 -- [ Math, String, Stack, Recursion ]

  Problem Statement:
  - Given a valid mathematical expression that contains brackets, the + and - operators, and multi-digit numbers,
    evaluate the expression

  Approach:
  - What's important is respecting the brackets, inner brackets to be evaluated before the outer ones
  - There is a recursive structure where for: (1+(4+5+2)-3)+(6+8)
    - You see 4+5+2 as a sub-problem and call the recursive func again to solve it
  - Hence, we see that the start of a new sub-problem is indicated by an opening bracket, and delimited by its
    corresponding closing bracket
  - so for eg in (-5+(6-(7+(9+8)))), we will recurse 4 times till we reach 9+8, eval it, and go back up

  - SO: We also see that instead of recursion, if we just maintain a separate stack entry for each pair of opening
    and closing brackets...
  - The stack entries will look like [-5, 6, -7, 9+8]
  - Then we reach the 4 closing brackets, and the last stack entry is popped and combined with the one before it
  - THIS is the approach to solve this problem

  Additional bookkeeping:
  - We need to know the sign of the current number under consideration, and the signs for all the brackets, these
    are the units of our expression
  - Use a var to track the sign of the current number (as 1 or -1, multiply to get the val when needed)
  - For the latter, the stack entry will look like (sign (1 or -1), <value of the expr inside this pair of brackets>)
  - Notice that when a bracket is encountered, the running sign gets assigned to the stack entry, and the running
    sign then resets to positive
    - In simple words: -(1+2+3), for this, stack entry sign is negative, val inside is positive sign by default
    - Makes things simpler
"""


NOT_DIGITS = {' ', '(', ')', '+', '-'}


class Solution:
    def calculate(self, s: str) -> int:
        # stack entry format: (multiplier, value)
        # approach: create new stack entry everytime a bracket is encountered
        # maintain total for that bracket in the stack entry
        # when bracket is closed, flush the stack entry into the previous one
        cur_sign = 1
        stack = [[1, 0]]
        i = 0
        while i < len(s):
            if s[i] == ' ':
                pass
            elif s[i] == '(':
                stack.append([cur_sign, 0])
                cur_sign = 1
            elif s[i] == ')':
                popped = stack.pop()
                stack[-1][1] += popped[0]*popped[1]
            elif s[i] == '+':
                cur_sign = 1
            elif s[i] == '-':
                cur_sign = -1
            else:
                e = i+1
                while e < len(s) and s[e] not in NOT_DIGITS:
                    e += 1
                stack[-1][1] += cur_sign * int(s[i:e])
                i = e-1
            i += 1
        return stack[-1][0] * stack[-1][1]
