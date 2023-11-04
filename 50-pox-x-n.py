"""
Use binary exponentiation to calculate x^n
Example: 2^10
Binary exponentiation:
- res = 2 (start), pow=1
- res*=res -> 4, pow=2
- res*=res -> 8, pow=4
- res*=res -> 16, pow=8

- Here, in 3 steps, we calculated up to a power of 8
- basically, we start with x, square it, assign the result to x and do this in a recursive manner
- on every step, the power we're at squares, but we stop before we leapfrog the target power
- so target: 10, we do binary exponentiation to take a shortcut to power=8, then we switch back to the normal linear
  algorithm and multiply res by x by 2 twice (twice because 10-8), to reach the correct result

Edge cases:
- If the input number is negative, then there's a change we might lose its sign in the binary exponentiation phase
  if the phase goes on for an even number of cycles (eg: -2^8): -2*-2 = 4*4 = 16
- so just remember if its negative and n is odd

- in some cases the number stays the same, like when x=1, or when x=0, or when x is something else but it
  goes to 0, in these cases detect if the new res is the same as the previous in the binary exponentiation phase, if so,
  early return
"""


class Solution:
    def myPow(self, x: float, n: int) -> float:
        pw = 2
        if n == 0:
            return 1
        flip_negative = x < 0 and n % 2
        if flip_negative:
            x = -x
        if n < 0:
            n = -n
            x = 1 / x
        prev_res = res = x
        while pw <= n:
            pw *= 2
            prev_res = res
            res *= res
            # print(res, pw)
            if res == prev_res:
                return res if not flip_negative else -res
        for _ in range(pw // 2, n):
            res *= x
        return res if not flip_negative else -res
        # 268435456
        # 536870912
        # 1073741824
        # 2147483648
        # 2147483647
