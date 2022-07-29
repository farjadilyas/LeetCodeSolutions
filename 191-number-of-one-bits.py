"""
  191. Number of 1 bits
  [ Easy ] | [ 63.1% ] -- Solved 26/07/2022 -- [ Bit Manipulation, Divide and Conquer ]

  Problem Statement:
  - Given a number, return the number of 1s in its binary representation
"""

"""
  APPROACH: MOD AND DIVIDE
  - Divide by 10 to right shift, mod 2 to get the right most bit
  - Check if bit is one and increment count, continue to divide till number is 0 (all bits that could be set have been
    checked)

  Time Complexity: O(logN) - divide by base 10 at every step, so logbase10(N)
  Space Complexity: O(1)
"""


def hammingWeight(self, n: int) -> int:
    count = 0
    while n > 0:
        if n % 2 == 1:
            count += 1
        n = int(n / 2)
    return count


"""
  APPROACH: BIG BRAIN BIT MANIPULATION
  - Attempt to count the set bits directly, skipping the 0 bits entirely, not even looping for them
  - IDEA: subtracting by one either unsets the set LSB or right shifts it by 1
    - Hence, n&(n-1) will force the set LSB to be unset - two cases:
      - 11 & 10 -> 10
      - 10 & 01 -> 00
    - We can continue with this operation until n is zero

  - Hence, the number of loops = the number of set digits, which are at most logN
  
  Time Complexity: O(logN) - but much better average case
  Space Complexity: O(1)
"""


def hammingWeight(self, n):
    count = 0
    while n > 0:
        n = n&(n-1)
        count += 1
    return count
