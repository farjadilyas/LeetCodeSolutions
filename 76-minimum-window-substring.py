"""
  211. Minimum Window Substring
  [ Hard ] | [ 40.8% ] -- Solved 19/02/2023 -- [ Sliding Window, Hash Table, String ]
  ----------- {{ SUBMISSION STATS }} --------------
  FASTER THAN:99.4%
  MEMORY USAGE: 76.9%

  Problem Statement:
  - Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that...
  - every character in t (including duplicates) is included in the window. If there is no such substring,
    return the empty string "".

  Approach:
  - NOTE: This question is similar to longest repeating character replacement
  - In simple words, we have to find the minimum length substring of s which has a frequency distribution that is
    the upper bound of t's frequency distribution (frequency of all characters in s > that of those in c)

  - Build the target frequency distribution for string t
  - Initialize a running frequency distribution, use None to easily identify characters that don't occur
  - Set counts to all distinct characters in string t, so we know how many frequencies we have to set to zero
  - Keep track of the number of frequencies set to zero in 'zeros'

  - Create a sliding window, expand it till the running frequency distribution is the upper bound of the target
  - This is true when zeros = counts
  - When the window is valid, minimize it from the head size to arrive at the optimal answer for the string we have
    parsed till now (reason for minimizing is that if s = AABC, t = ABC, then the window will initially span all of s,
    but can then be minimized from the head side to arrive at the optimal solution
  - Remember to keep the zeros up to date
  - Optimization
    - When we have found a valid window, we will now only be interested in windows that are smaller
    - So move the head forward by 2 steps once a valid window is found to reduce the length of the window by 1 for the
      next iteration, tail always moves forward
    - We will not let the window expand beyond this length, so once any valid window is found, head will keep moving
      forward by 1
    - You can come up with a proof for why it is safe to discard the 2nd character after head if the current window is
      valid

  Time Complexity: O(N) - len(s)
  Space Complexity: O(M) - Number of distinct characters
"""


"""
  UPDATE - NEW, MUCH SIMPLER SOLUTION BELOW - FIND OG SOLUTION AT THE BOTTOM
"""


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counts = [0 for _ in range(128)]
        for c in t:
            counts[ord(c)] += 1
        num_matches = sum(not c for c in counts)
        start = 0
        min_start, min_end = 0, 100_000
        for end in range(len(s)):
            counts[ord(s[end])] -= 1
            if counts[ord(s[end])] == 0:
                num_matches += 1
            while start < len(s) and counts[ord(s[start])] < 0:
                counts[ord(s[start])] += 1
                start += 1
            if num_matches == 128 and end - start < min_end - min_start:
                min_start, min_end = start, end
        return s[min_start:min_end+1] if min_end != 100_000 else ""


"""
  ORIGINAL SOLUTION
"""


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        zeros = target = start = 0
        counts = [None for _ in range(128)]

        # Build target freq dist
        for c in t:
            c_id = ord(c)
            if counts[c_id] is None:
                counts[c_id] = 1
                target += 1
            else:
                counts[c_id] += 1

        min_len = 100001
        min_bound_x, min_bound_y = None, None
        restrict_window = False
        for end, c in enumerate(s):
            c_id = ord(c)

            # Update the current frequency dist, and zeros count
            if counts[c_id] is not None:
                if counts[c_id] == 1:
                    zeros += 1
                counts[c_id] -= 1

            # If window is valid, minimize it
            update = zeros == target
            while zeros == target:
                h_id = ord(s[start])
                start += 1
                if counts[h_id] is None:
                    continue
                if counts[h_id] == 0:
                    zeros -= 1
                counts[h_id] += 1

            # If this window was valid, start keeping a constant window size and update the minimum window up till now
            if update:
                restrict_window = True
                if end - start + 2 < min_len:
                    min_len = end - start + 2
                    min_bound_x, min_bound_y = start - 1, end

            # If window size is being kept constant, then move the head of the window forward by one along with the tail
            if restrict_window and start < len(s):
                h_id = ord(s[start])
                start += 1
                if counts[h_id] == 0:
                    zeros -= 1
                if counts[h_id] is not None:
                    counts[h_id] += 1
        return s[min_bound_x:min_bound_y + 1] if min_bound_x is not None else ''
