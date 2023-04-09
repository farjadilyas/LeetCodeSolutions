"""
  17. Letter Combinations of a Phone Number
  [ Medium ] | [ 56.5% ] -- Solved 26/03/2023 -- [ Backtracking, Hash Table, String ]

  Problem Statement:
  - Given a string of integers, return a list of all possible output strings where each letter corresponds to its
    configured integer (see the hash map in the solution)

  Approach:
  - Simple backtracking solution
"""

class Solution:
    mp = {2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl', 6: 'mno', 7: 'pqrs', 8: 'tuv', 9: 'wxyz'}

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        res, ld = [], len(digits)

        def backtrack(cidx, cres):
            for c in self.mp[int(digits[cidx])]:
                if cidx == ld - 1:
                    res.append(''.join([*cres, c]))
                else:
                    backtrack(cidx + 1, [*cres, c])

        backtrack(0, [])
        return res
