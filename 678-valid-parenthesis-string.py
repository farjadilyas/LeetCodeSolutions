class Solution:
    def checkValidString(self, s: str) -> bool:
        # (*))
        # 1, 1
        # 0, 2
        # 0, 1
        # 0, 0

        leftMin = leftMax = 0
        for c in s:
            if c == '(':
                leftMin += 1
                leftMax += 1
            else:
                if leftMin != 0:
                    leftMin = leftMin-1
                leftMax += (-1 if c == ')' else 1)
                if leftMax < 0:
                    return False
        return leftMin == 0
