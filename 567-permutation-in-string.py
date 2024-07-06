"""
  567. Permutation in String
  [ Medium ] | [ 44.4% ] -- Solved 18/02/2023 -- [ Sliding Window, Hash Table, Two pointers ]

  Problem Statement:
  - Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
  - Basically, return true if there exists a substring in s2 that has the same frequency distribution as that of s1

  Approach:
  - Maintain a sliding window that contains a subset of the permutation at all times
  - Build the target frequency distribution, mark the chars that don't appear as None for easy identification
  - Maintain a count of the number of 'zeroes' encountered, the number of characters in the current window
    whose frequency exactly matches the target
  - Iterate through s2..
    - If the character does not appear in s1 (is marked None in the freq dist), then no valid window can contain that
      char, so start a new window beyond that char
    - Else, if the character's frequency has now exceeded the target, shrink the window from the head till this
      character's frequency is valid again, the window is guaranteed to be valid during shrinking since it will still
      be a valid subset of a permutation of s1
    - When changing the freq dist, update the zeros value accordingly
    - Once the # zeros = number of distinct characters in s1, return True, else return False

  - A less optimal solution compares the frequency distributions at each step O(26) to check whether the current
    window is a valid permutation of s1

  Time Complexity: O(N) - N: len(s2), M: # distinct characters
  Space Complexity: O(M)
"""

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        offset = ord('a')
        counts = [0] * 26
        if len(s2) < len(s1):
            return False
        for i in range(len(s1)):
            counts[ord(s1[i]) - offset] += 1
            counts[ord(s2[i]) - offset] -= 1
        num_ones = sum(bool(c) for c in counts)
        start = 0
        end = len(s1) - 1
        while end < len(s2) - 1:
            if not num_ones:
                return True
            outgoing_idx = ord(s2[start]) - offset
            counts[outgoing_idx] += 1
            if counts[outgoing_idx] == 1:
                num_ones += 1
            elif counts[outgoing_idx] == 0:
                num_ones -= 1
            start += 1
            end += 1
            incoming_idx = ord(s2[end]) - offset
            counts[incoming_idx] -= 1
            if counts[incoming_idx] == -1:
                num_ones += 1
            elif counts[incoming_idx] == 0:
                num_ones -= 1
        return not num_ones
