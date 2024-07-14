"""
This is the optimal solution for Basic Calculator 1, 2 and 3
"""

not_digits = {' ', '(', ')', '+', '-', '*', '/'}


class Solution:
    def calculate(self, s: str) -> int:
        # stack entry format: (multiplier, value)
        # approach: create new stack entry everytime a bracket is encountered
        # maintain total for that bracket in the stack entry
        # when bracket is closed, flush the stack entry into the previous one
        cur_sign = 1
        stack = [[1, 0]]
        i = 0
        cur_num = 0
        cur_op = None
        while i < len(s):
            if s[i] == '(':
                stack.append([cur_sign, 0])
                cur_sign = 1
            elif s[i] == ')':
                stack[-1][1] += cur_num
                cur_num = 0
                popped = stack.pop()
                stack[-1][1] += popped[0] * popped[1]
            elif s[i] == '+':
                stack[-1][1] += cur_num
                cur_num = 0
            elif s[i] == '-':
                stack[-1][1] += cur_num
                cur_num = 0
                cur_sign = -1
            elif s[i] == '*' or s[i] == '/':
                cur_op = s[i]
            elif s[i] != ' ':
                e = i + 1
                while e < len(s) and s[e] not in not_digits:
                    e += 1
                if not cur_op:
                    cur_num = cur_sign * int(s[i:e])
                elif cur_op == '*':
                    cur_num *= cur_sign * int(s[i:e])
                    cur_op = None
                elif cur_op == '/':
                    cur_num = int(cur_num / (cur_sign * int(s[i:e])))
                    cur_op = None
                cur_sign = 1
                i = e - 1
            i += 1
        stack[-1][1] += cur_num
        return stack[-1][0] * stack[-1][1]
