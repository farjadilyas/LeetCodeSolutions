"""
  79. Palindrome Partitioning
  [ Medium ] | [ 64.8% ] -- Solved 26/03/2023 -- [ Backtracking, Dynamic Programming, String ]

  Problem Statement:
  - Return all possible partitions of strings where each substring in a partition is a palindrome
  - Simple DFS backtracking solution, go over the string, capture substrings of lengths 1 - max, and do the palindrome
    check + recursive call

  Optimization:
  - Can use DP to memoize whether a substring is a palindrome or not for each starting and ending index
  - Turns O(N) palindrome check into O(1)
"""


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, ls = [], len(s)
        def backtrack(pos, cres):
            for i in range(pos, ls):
                if any(s[j] != s[i-(j-pos)] for j in range(pos, i+1)):
                    continue
                if i+1 >= ls:
                    res.append([*cres, s[pos:i+1]])
                else:
                    backtrack(i+1, [*cres, s[pos:i+1]])
        backtrack(0, [])
        return res

# Using Dynamic Programming to do O(1) palindrome check instead of O(N)
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, ls = [], len(s)
        dp = [[False for j in range(ls)] for i in range(ls)]
        def backtrack(pos, cres):
            for i in range(pos, ls):
                if (i-pos < 2 or dp[pos+1][i-1]) and s[i] == s[pos]:
                    dp[pos][i] = True
                    if i+1 >= ls:
                        res.append([*cres, s[pos:i+1]])
                    else:
                        backtrack(i+1, [*cres, s[pos:i+1]])
        backtrack(0, [])
        return res
