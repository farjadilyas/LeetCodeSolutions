"""
  39. Combination Sum
  [ Medium ] | [ 68.6% ] -- Solved 25/03/2023 -- [ Array, Backtracking ]

  Problem Statement:
  - Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations
    of candidates where the chosen numbers sum to target. You may return the combinations in any order.

  Approach:
  - Similar to [39 - Subsets], do a DFS traversal, only move forward in the candidtae array to avoid duplicates
  - Only addition upon the Subsets problem is: for each candidate, explore using it multiple times as long as the target
    isn't exceeded as a result of exploring a path with an additional instance of the candidate

  Time Complexity: O(2^N)
  Space Complexity: O(N)
"""

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res, self.candidates, self.target = [], candidates, target
        self.recurse(0, [], 0)
        return self.res

    def recurse(self, cidx, cres, ctotal):
        for nidx in range(cidx, len(self.candidates)):
            ntotal = ctotal + self.candidates[nidx]
            nres = [*cres]
            while ntotal <= self.target:
                nres.append(self.candidates[nidx])
                if ntotal == self.target:
                    self.res.append(nres)
                    break
                self.recurse(nidx + 1, [*nres], ntotal)
                ntotal += self.candidates[nidx]
