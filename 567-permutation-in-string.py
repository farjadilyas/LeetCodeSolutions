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
        od = [None for _ in range(26)]
        target = 0
        for c in s1:
            c_id = ord(c) - 97
            if od[c_id] is None:
                od[c_id] = 1
                target += 1
            else:
                od[c_id] += 1

        start = zeros = 0
        for end, c in enumerate(s2):
            c_id = ord(c) - 97
            # Shrink window if an invalid character is found (not present in string, or one too many)
            while (od[c_id] is None and start != end + 1) or (od[c_id] is not None and od[c_id] <= 0):
                h_id = ord(s2[start]) - 97
                if od[h_id] is not None:
                    if od[h_id] == 0:
                        zeros -= 1
                    od[h_id] += 1
                start += 1
            # Once window is valid, update it with the current char
            if od[c_id] is not None:
                od[c_id] -= 1
                if od[c_id] == 0:
                    zeros += 1

            if zeros == target:
                return True
        return False
