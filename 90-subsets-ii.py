class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.res, self.nums = [[]], nums
        nums.sort()
        self.recurse(0, [])
        return self.res

    def recurse(self, cidx, cres):
        prev = None
        for nidx in range(cidx, len(self.nums)):
            if self.nums[nidx] == prev:
                continue
            prev = self.nums[nidx]
            nres = [*cres, self.nums[nidx]]
            self.res.append(nres)
            self.recurse(nidx + 1, nres)