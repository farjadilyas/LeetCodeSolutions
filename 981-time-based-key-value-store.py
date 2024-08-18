from math import ceil
from collections import defaultdict


def alt_bisect(low, high, condition):
    """
    This bisect finds the last T in [T, T, T, F, F, F, F]
    Since low can be equal to middle, if condition(middle) is false it'll lead to an infinite recursion
    So here we take the ceil of division to get the middle, not the floow

    Not recommended to use this for problems where you need to find the last T in [T, T, T, F, F, F, F]
    It is better to use our normal bisect template, but just flip the search by using len(nums)-1-idx in the condition
    lambda to effectively reverse the array, and remember to do the same to the result of the bisect
    """
    while low < high:
        middle = ceil((low + high) / 2)
        # print(f"middle {middle} {low} {high}")
        if condition(middle):
            low = middle
        else:
            high = middle - 1
    return low


def bisect(low, high, condition):
    """
    Our typical bisect template

    Notable improvement: can do a condition check on the result before returning to avoid checks on the caller side
    This simple check is possible due to the low < high condition (rather than <= high) which ensures both low and high
    never go outside the valid index range
    """
    while low < high:
        middle = (low + high) // 2
        if condition(middle):
            high = middle
        else:
            low = middle + 1
    return low if condition(low) else -1


class TimeMap:
    """
    Since our bisect template finds the first T in [F, F, F, F, T, T, T]
    But the nature of our problem is find the last T in [T, T, T, F, F, F, F]

    So: Find the first value at a greater timestamp than the query timestamp, and move one to the left
    This turns the problem into [F, F, F, T, T, T, T] - Find the first T using bisect, and get the left element
    """

    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map: return ""
        nums = self.map[key]
        next_idx = bisect(
            low=0,
            high=len(nums)-1,
            condition=lambda idx: nums[idx][1] > timestamp
        )
        # If next_idx==0, then no elements came before query ts, if next_idx=-1, then all elements came before
        if next_idx == 0:
            return ""
        if next_idx == -1:
            return nums[-1][0]
        return nums[next_idx-1][0]
