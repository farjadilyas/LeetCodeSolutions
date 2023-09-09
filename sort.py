import copy
import heapq

a = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]


def bubble_sort(nums):
    for itr in range(len(nums)):
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                nums[i-1], nums[i] = nums[i], nums[i-1]
    return nums


def selection_sort(nums):
    """
    Selection sort: Nested loop, first loop increases the sorted partition (builds from the smallest number),\
    nested loop finds the minimum in the unsorted partition and swaps it with the tail of the sorted partition -
    thereby extending the sorted partition by 1
    """
    if not nums:
        return nums
    for sorted_len in range(len(nums)):
        mn_idx, mn = sorted_len, nums[sorted_len]
        for i in range(sorted_len, len(nums)):
            if nums[i] < mn:
                mn_idx, mn = i, nums[i]
        if mn_idx != sorted_len:
            nums[mn_idx], nums[sorted_len] = nums[sorted_len], nums[mn_idx]
    return nums


def insertion_sort(nums):
    """
    Outer loop simply traverses array, nested loop swaps the element that is being considered till its in a sorted pos
    """
    for i in range(1, len(nums)):
        cursor = i
        while cursor > 0 and nums[cursor] < nums[cursor-1]:
            nums[cursor-1], nums[cursor] = nums[cursor], nums[cursor-1]
            cursor -= 1
    return nums


class QuickSort:
    def __init__(self, nums):
        self.nums = nums

    def execute(self):
        self.quick_sort(0, len(self.nums)-1)
        return self.nums

    def quick_sort(self, low, high):
        if low >= high:
            return
        pivot_idx = self.partition(low, high)
        self.quick_sort(low, pivot_idx-1)
        self.quick_sort(pivot_idx+1, high)

    def partition(self, low, high):
        pivot_idx = (low+high)//2
        pivot = self.nums[pivot_idx]
        self.nums[high], self.nums[pivot_idx] = self.nums[pivot_idx], self.nums[high]
        left_wall = low
        for rightWall in range(low, high+1):
            if self.nums[rightWall] < pivot:
                self.nums[left_wall], self.nums[rightWall] = self.nums[rightWall], self.nums[left_wall]
                left_wall += 1
        self.nums[left_wall], self.nums[high] = self.nums[high], self.nums[left_wall]
        return left_wall


class MergeSort:
    def __init__(self, nums):
        self.nums = nums
        self.buffer = [0 for _ in range(len(nums))]

    def execute(self):
        self.merge_sort(0, len(self.nums)-1)
        return self.nums

    def merge_sort(self, low, high):
        # Return if size of partition is 1
        if high - low < 1:
            return

        # Divide into two partitions
        middle = (low + high) // 2
        p1, p2, r = low, middle + 1, 0
        self.merge_sort(low, middle)
        self.merge_sort(middle+1, high)

        # Take the partitions you made above, start at their heads and pick the smaller one, and move forward
        # Fill the buffer as you go, we will flush it to the true array in the end
        # Implementing an in-place merge sort is non-trivial, so the usual impl (this one) is O(N) space complexity
        while p1 <= middle and p2 <= high:
            if self.nums[p1] < self.nums[p2]:
                self.buffer[r] = self.nums[p1]
                r += 1
                p1 += 1
            else:
                self.buffer[r] = self.nums[p2]
                r += 1
                p2 += 1
        pe, limit = (p2, high) if p1 > middle else (p1, middle)
        while pe <= limit:
            self.buffer[r] = self.nums[pe]
            r += 1
            pe += 1
        for i in range(r):
            self.nums[low+i] = self.buffer[i]


class Heap:
    def __init__(self, nums):
        self.nums = nums

    def sort(self):
        ...


def count_sort(nums):
    ...


def radix_sort(nums):
    ...


if __name__ == '__main__':
    print(bubble_sort(copy.deepcopy(a)))
    print(selection_sort(copy.deepcopy(a)))
    print(insertion_sort(copy.deepcopy(a)))
    print(QuickSort(nums=copy.deepcopy(a)).execute())
    print(MergeSort(nums=copy.deepcopy(a)).execute())
