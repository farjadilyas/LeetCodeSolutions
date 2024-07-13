"""
  20. Valid Parenthesis
  [ Easy ] | [ 40.8% ] -- Solved 26/07/2022 -- [ String, Stack ]

  Problem Statement:
  - Given 3 possible types of parenthesis and a parenthesis string, check whether the string is a valid parenthesis
    string

  Approach:
  - The counting approach won't work here (keeping track of the number of opened brackets and making sure they don't
    go below 0, and are 0 at the end) because:
    - A CLOSING BRACKET MUST CLOSE THE CLOSEST UNMATCHED OPENING BRACKET OF THE SAME TYPE
    - ([)] - this example would pass in the counting approach, since the brackets are in the correct order if you
      look at one particular type, but '[)]' is incorrect since ([) has an unmatched [ in the middle
    - Hence, use a stack to track the actual types that need to be closed
  - Due to the rule above (in caps) - we must maintain a stack of the unmatched opening brackets in the order they
    appear in

  Algorithm:
  - Loop through string
  - If opening bracket, simply add it to the stack, no validation necessary
  - If closing bracket, it MUST close an opening bracket of the right type, if not return False.
    - If it does close an opening bracket, the opening bracket must be popped
    - No closing brackets will ever be part of the stack, closing brackets will always cancel out opening brackets

  Time Complexity: O(N)
  Space Complexity: O(N)
"""

CLOSING_OPENING_PAIRS = {
    ')': '(',
    '}': '{',
    ']': '[',
}


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in CLOSING_OPENING_PAIRS:
                if not stack or stack.pop() != CLOSING_OPENING_PAIRS[c]:
                    return False
            else:
                stack.append(c)
        return not stack
