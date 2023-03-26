"""
  46. Permutations
  [ Medium ] | [ 75.6% ] -- Solved 25/03/2023 -- [ Array, Backtracking ]

  Problem Statement:
  - Given an integer array with unique elements, return all subsets of the array, without any duplicates

  Approach:
  - Do a DFS traversal, where each branch maintains its own result array, the result is obtained at the leaf nodes,
    the running results array branches whenever the traversal branches
  - Restrict the traversal options to elements that are further ahead in the array than the current one, this
    restriction alone is enough to prevent duplicate subsets in the final result

  Time Complexity: O(N*N!)
  Space Complexity: O(N)
"""

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res, self.nums, self.cres, self.ln = [], nums, [None for i in range(len(nums))], len(nums)
        self.recurse(0)
        return self.res

    def recurse(self, depth):
        for idx, c in enumerate(self.nums):
            if c is None:
                continue
            self.nums[idx] = None
            self.cres[depth] = c
            if depth + 1 == self.ln:
                self.res.append(self.cres[:])
            else:
                self.recurse(depth + 1)
            self.nums[idx] = c
