"""
  16. 3Sum Closest
  [ Medium ] | [ 57.7% ] -- Solved 04/12/2022
  ----------- {{ SUBMISSION STATS }} --------------
  FASTER THAN: 58.30%
  MEMORY USAGE: 97.11%

  Problem:
  - Standard 3 sum problem, but instead of finding the 3sum that adds up to target, we need to find the 3sum that is
    closest to the target. Can assume there will be exactly one answer

  Approach:
  - Any of the methods that work on the 3Sum problem can work here except for the hashset one, since we don't
    have a specific target to look up.. we just want the closest sum
  - Below, we'll use the sort then two-pointer approach
  - Keep in mind breaking from the inner 2-pointer loop early in any way isn't going to work
    - eg: 1,2,3,4,4.75,5 - target=9.75, once sum goes over, need to constrict from the RHS
  - So it's completely like the 3sum solution, however...
  - we use cur_target = target - nums[first_idx], so be careful to derive the best sum at the end correctly (see comments)

  Time Complexity: O(N^2) - Same as standard 3sum - sorting: NlogN, then N in outer iter nested w/ N in inner two pointer
  Space Complexity: O(N) - For sorting
"""

class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        min_distance = 500_001
        # target = nums[first_idx] + nums[second_idx] + nums[third_idx]
        # min_distance = target - best_sum
        # best_sum = target - min_distance
        # Don't store abs in min_distance since its imp to calc best_sum
        for first_idx in range(len(nums)-2):
            second_idx = first_idx+1
            third_idx = len(nums)-1
            while second_idx < third_idx:
                cur_target = target - nums[first_idx]
                cur_sum = nums[second_idx] + nums[third_idx]
                cur_distance = cur_target - cur_sum
                if abs(cur_distance) < abs(min_distance):
                    min_distance = cur_distance
                if cur_sum == cur_target:
                    return target
                elif cur_sum > cur_target:
                    third_idx -= 1
                else:
                    second_idx += 1
        return target - min_distance
