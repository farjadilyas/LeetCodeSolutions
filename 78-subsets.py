"""
  78. Subsets
  [ Medium ] | [ 74.8% ] -- Solved 25/03/2023 -- [ Array, Backtracking, Bit Manipulation ]

  Problem Statement:
  - Given an integer array with unique elements, return all subsets of the array, without any duplicates

  Approach:
  - Do a DFS traversal, where each branch maintains its own result array, the result is obtained at the leaf nodes,
    the running results array branches whenever the traversal branches
  - Restrict the traversal options to elements that are further ahead in the array than the current one, this
    restriction alone is enough to prevent duplicate subsets in the final result

  Time Complexity: O(2^N)
  Space Complexity: O(N) - Max traversal depth of N will be reached for subset that is the same as the input
"""

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res, self.nums = [[]], nums
        self.recurse(0, [])
        return self.res

    def recurse(self, cidx, cres):
        for nidx in range(cidx, len(self.nums)):
            nres = [*cres, self.nums[nidx]]
            self.res.append(nres)
            self.recurse(nidx + 1, nres)
