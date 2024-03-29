"""
  3. Longest Substring without repeating characters

  Approach 1:
  - Create a sliding window from the start, expand it till a duplicate character is found, disregard the previous
    occurrence of the duplicate character (by bringing the head of the sliding window to the element following the
    previous occurrence so that the sliding window remains the largest it can be without a duplicate character
  - Desired properties:
    - Information about which characters are in the sliding window should be maintained
    - Should know where the prev occurrence of the duplicate character occurred within the sliding window so that
      the duplicate character and all the characters preceeding it can be removed from the sliding window

  Solution for Approach 1:
  - Create an array of size: range of characters
  - Iterate over the array, for each character, store the largest index it has occurred at so far
  - Remember where the sliding window started by saving the largest index encountered for the head of the sliding window
  - This way, the following crucial operations can be done in constant time:
    - is a character duplicate: previous occurrence index >= sliding window head character's largest index
    - remove duplicate and all preceeding characters: update the sliding window head,
      set it = previous occurrence index + 1 of the duplicate character

  Summary:
  - Iterate through array (and maintain the max sliding window length)
    - If character is duplicate, update window head
    - Update the largest index for the current character

    Time Complexity: O(N)
    Space Complexity: O(1)
"""


def lengthOfLongestSubstring(self, s: str) -> int:
    # Latest index of occurrence for each character
    occurance_idx = [-1] * 128
    # Store the occurrence index of the head of the sliding window
    attempt_idx = 0
    max_len = 0
    for i, c in enumerate(s):
        c_id = ord(c)
        # If the current character occurred beyond the head of the current window, it is duplicate
        # Calculate the max length of this expansion of the window, advance the head of the window just beyond the
        # previous occurrence of the duplicate character so it is valid again
        if occurance_idx[c_id] >= attempt_idx:
            max_len = max(max_len, i - attempt_idx)
            attempt_idx = occurance_idx[c_id] + 1
        occurance_idx[c_id] = i
    max_len = max(max_len, len(s) - attempt_idx)
    return max_len
