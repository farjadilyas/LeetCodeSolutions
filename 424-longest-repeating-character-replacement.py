"""
  424. Longest Repeating Character Replacement
  [ Medium ] | [ 51.8% ] -- Solved 18/02/2023 -- [ Sliding Window, Hash Table, String ]

  Problem Statement:
  - You are given a string s and an integer k. You can choose any character of the string and change it to any
    other uppercase English character. You can perform this operation at most k times.
  - Return the length of the longest substring containing the same letter you can get after performing the above
    operations.
"""


"""
  Slow Sliding Window Approach (suboptimal):
  - Key idea: The validity of the sliding window can be checked by window_length - max(counts) <= k
  - In a given window, we want to take the most common letter and replace all other letters with it to have a
    homogenous string with the fewest replacements
  - Create a sliding window, maintain counts for each valid letter
  - Extend the window using the formula, if its invalid, shrink it till it becomes valid
  - For this impl.., given n = len(s), m = number of distinct characters (26)
    - Time Complexity: O(MN)
    - Space Complexity: O(M)

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
        start = end = 0
        counts = [0] * 26
        offset = ord('A')
        ls = len(s)
        while end < ls:
            counts[ord(s[end])-offset] += 1
            if end-start+1 - max(counts) > k:
                counts[ord(s[start])-offset] -= 1
                start += 1
            end += 1
        return end - start


"""
    Optimal Approach:
    - There's no need to get max(counts) inside the nested loop, can just maintain the max_frequency seen so far
    - IMPORTANT: The optimization here is using the max frequency seen in any window so far rather than the
      max frequency of the current window (for the > k check).
      This works since if a window has a max frequency less than the global max frequency, this window 
      cannot beat the window that yielded the global max frequency.
      This way we avoid having to do a max(counts) inside the nested loop and remove M from the time complexity.
    
     Time Complexity: O(N)
     Space Complexity: O(M)
     Beats 99.6% in both time and space
"""
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start = end = 0
        counts = [0] * 26
        offset = ord('A')
        max_frequency = 0
        while end < len(s):
            c_id = ord(s[end])-offset
            counts[c_id] += 1
            if counts[c_id] > max_frequency:
                max_frequency = counts[c_id]
            if end-start+1 - max_frequency > k:
                counts[ord(s[start])-offset] -= 1
                start += 1
            end += 1
        return end - start
