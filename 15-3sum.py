class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        ln = len(nums)
        for i in range(ln):
            if i and nums[i] == nums[i-1]:
                continue
            target = -nums[i]
            start, end = i+1, ln-1
            while start < end:
                res = nums[start] + nums[end]
                if res == target:
                    result.append([-target, nums[start], nums[end]])
                    start += 1
                    while start < ln and nums[start] == nums[start-1]:
                        start += 1
                    end -= 1
                elif res > target:
                    end -= 1
                else:
                    start += 1
        return result
