"""
  424. Longest Repeating Character Replacement
  [ Medium ] | [ 51.8% ] -- Solved 18/02/2023 -- [ Sliding Window, Hash Table, String ]

  Problem Statement:
  - You are given a string s and an integer k. You can choose any character of the string and change it to any
    other uppercase English character. You can perform this operation at most k times.
  - Return the length of the longest substring containing the same letter you can get after performing the above
    operations.

  Approach:
  - Key idea: The validity of the sliding window can be checked by window_length - max(counts) <= k
  - In a given window, we want to take the most common letter and replace all other letters with it to have a
    homogenous string with the fewest replacements
  - Create a sliding window, maintain counts for each valid letter
  - Extend the window using the formula, if its invalid, shrink it till it becomes valid
  - For this impl.., given n = len(s), m = number of distinct characters (26)
    - Time Complexity: O(mn)
    - Space Complexity: O(m)

  OPTIMAL SOLUTION
  - This solution uses the idea: At every step, we just need the maximum frequency to keep track of validity
  - If we maintain max freq in a variable, rather than doing a pass to calculate it, it remains valid until the
    window is shrunk. We need one more pass everytime it is shrunk to recalculate the max
  - To avoid recalculating the max, we need to avoid shrinking the sliding window
  - One way we can do that is: Whenever the window becomes invalid, keep it the same size and move it along till it is
    valid again
  - How will we know once its valid? When the frequency of the char encountered is greater than the max freq
  - We only care about the max length possible for the window, for that to increase, max freq needs to increase
  - There may be smaller valid windows when we're moving the invalid window along, but we don't care about those
    since they don't affect the answer, so we'll just wait till we find a sequence that can extend the best window we
    found so far
"""

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        head = tail = 0
        counts =[0 for _ in range(26)]
        max_len = 0
        for c in s:
            counts[ord(c)-65] += 1
            if tail-head+1 - max(counts) > k:
                max_len = max(max_len, tail-head)
            # Shrink window
            while tail-head+1 - max(counts) > k:
                counts[ord(s[head])-65]-=1
                head+=1
            tail += 1
        max_len = max(max_len, tail-head)
        return max_len
