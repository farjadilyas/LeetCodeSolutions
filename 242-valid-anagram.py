"""
  242. Valid Anagram
  [ Easy ] | [ 61.9% ] -- Solved 26/07/2022 -- [ HashTable, String ]

  Problem Statement:
  - Given two strings, tell if they're anagrams of each other
"""

"""
  APPROACH: USE COUNT ARRAY
  - Convert char to ascii to indices
  - In one pass, direct access to count array, one string can increment character counts, the other can decrement
  - Since anagrams require the frequency distribution over the alphabet for both strings to be the same, with the above
    strategy, if the strings are anagrams, then the count array will be zero in the end
  - Execute that strategy, and check if the count array is zero, if so, they are anagrams
  
  Time Complexity: O(N)
  Space Complexity: O(1)
"""


def isAnagram(self, s: str, t: str) -> bool:
    dp = [0 for _ in range(26)]
    s_len = len(s)
    if s_len != len(t):
        return False

    for i in range(s_len):
        dp[ord(s[i]) - 97] += 1
        dp[ord(t[i]) - 97] -= 1

    for i in dp:
        if i != 0:
            return False
    return True
