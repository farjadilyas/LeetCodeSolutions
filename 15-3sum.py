"""
TODO: write up

"""


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


"""
  No-Sort solution
  - Sorting gives us the following two advantages:
    - Enables the two-pointer 2sum solution, without sorting we have to use the hashset 2sum solution
    - Allows us to avoid dups easily since in both the outer and inner loops we can increment over dups

  - So if we have to remove sorting:
    - We have to use the hashset 2sum solution
    - We need to figure out a way to deal with dups

  - DEALING WITH DUPs in a no-sort solution
    - Maintain a hashset for the values encountered in the outer loop to skip dups for that
    - In the inner loop, sort each result triplet and store it in a hashset
    
  - Practically, no-sort is slower, less obvious, and less flexible if you need to come up with a solution for an
    alternative version of 3sum, but its a good exercise
"""


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        outer_set = set()
        hm = {num: None for num in nums}
        res = set()
        for i in range(len(nums)):
            if nums[i] in outer_set:
                continue
            outer_set.add(nums[i])
            for j in range(i+1, len(nums)):
                target = -nums[i]-nums[j]
                if hm.get(target) == i:
                    res.add(tuple(sorted([nums[i], nums[j], target])))
                hm[nums[j]] = i
        return list(res)
