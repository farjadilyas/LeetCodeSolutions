class Solution:
    def reverse(self, x: int) -> int:
        MAX_QUOTIENT = 214748364
        MAX_REMAINDER = 7

        digit_count = ans = 0
        flip = x < 0
        if flip:
            x *= -1
        while x:
            x, rem = divmod(x, 10)
            if digit_count == 9 and (ans > MAX_QUOTIENT or (ans == MAX_QUOTIENT and rem > MAX_REMAINDER)):
                return 0
            ans = ans * 10 + rem
            digit_count += 1
        return -ans if flip else ans
