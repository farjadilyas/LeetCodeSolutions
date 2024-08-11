from typing import Callable


class Bisect:
    """
    Most basic binary search solution

    Good for finding an EXACT match
    """
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums)-1
        while start <= end:
            middle = (start + end) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                start = middle+1
            else:
                end = middle-1
        return -1


def generic_bisect(nums: list[int], first_match_condition: Callable[[int], bool]) -> int:
    """
    Flexible binary search solution

    This solution tries to find the smallest index that satisfies a given condition

    Eg: Given a search space that gives the following when mapped with ``condition``:
    [FALSE, FALSE, FALSE, TRUE, TRUE, TRUE, TRUE]

    This implementation will find the index of the first TRUE

    Advantage: Keeps binary search simple, defers the heavy lifting to deducing the condition that will work and the
    post-processing required to return the correct answer
    """
    low, high = 0, len(nums)
    while low < high:
        mid = (low + high) // 2
        if first_match_condition(nums[mid]):
            high = mid
        else:
            low = mid + 1
    return low


class BisectLeftSolution:
    def search(self, nums: list[int], target: int) -> int:
        # [3,4,5,6,6,6,6,7,8,9]
        insert_left = generic_bisect(
            nums=nums,
            first_match_condition=lambda num: num >= target
        )
        # Index of first match can be:
        # = len(nums) if all elements are smaller than target
        # != index_of_target if target isn't present and there's an element bigger than target
        # == index_of_first_target if target is present

        # We only want to return when element on the matching index is target
        return insert_left if insert_left < len(nums) and nums[insert_left] == target else -1


class BisectRightSolution:
    def search(self, nums: list[int], target: int) -> int:
        # [3,4,5,6,6,6,6,7,8,9]
        insert_right = generic_bisect(
            nums=nums,
            first_match_condition=lambda num: num > target
        )
        # Index found is first index with element greater than target
        # so if target exists, nums[target-1] should be equal to target
        return insert_right - 1 if nums[insert_right - 1] == target else -1
