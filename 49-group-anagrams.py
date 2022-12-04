"""
  49. Group Anagrams
  [ Medium ] | [ 66.5% ] -- Solved 3/12/2022 -- [ HashTable, Arrays ]

  Problem Statement:
  - Given an array of strings, put the strings in groups based on whether they're anagrams of each other
"""

"""
  APPROACH: HASHABLE IDENTITY OF A PARTICULAR GROUP
  - Have to find something common between strings that are anagrams of each other, make it hashable, and use it as the
    keys to the hashtable that stores the groups of anagrams
  
  OPTION 1: All strings that are anagrams of each other have the frequency distribution of alphabets in common
  - Create an array, build the freq dist for each string, convert it to a tuple to make it hashable, use it as the
    key to a hashtable that contains the result subarray of strings that are anagrams of each other

  Time Complexity: O(NM) - if every string is of length M
  Space Complexity: O(N)
"""


def groupAnagrams(self, li: List[str]) -> List[List[str]]:
    dps = [[0 for _ in range(26)] for j in range(len(strs))]
    res = []
    hm = {}
    for idx, s in enumerate(strs):
        dp = dps[idx]
        for c in s:
            dp[ord(c)-97]+=1
        dp = tuple(dp)
        if dp in hm:
            hm[dp].append(s)
        else:
            nw = [s]
            res.append(nw)
            hm[dp] = nw
    return res

"""
OPTION 2:
- Another thing strings that are anagrams of each other have in common is that, when sorted, they are the same string
- Hence, instead of building a frequency distribution to arrive at a hash, the string can be sorted to arrive at the key
  since it is common between a group of strings that are anagrams of each other
- Increased runtime complexity due to sorting, but will use less memory provided that the strings used aren't pretty
  long
  
Time complexity: O(NMlogM)
Space complexity: O(N)
"""
def groupAnagrams(self, li: List[str]) -> List[List[str]]:
    dictionary = {}
    for word in li:
        sortedWord = ''.join(sorted(word))
        if sortedWord not in dictionary:
            dictionary[sortedWord] = [word]
        else:
            dictionary[sortedWord] += [word]
    return [dictionary[i] for i in dictionary]
