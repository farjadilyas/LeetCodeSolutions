"""
  167. Two Sum II
  [ Medium ] | [ 59.8% ] -- Solved 25/07/2022

  Problem:
  - Given an array sorted in ascending order
  - Return the indices of two numbers that add up to a target number


"""


"""
  APPROACH #1: Binary Search
  - Loop over the array, for a number n, the desired paired number is target - n
  - Use binary search to find that number

  MISSED OPPORTUNITY:
  - This solution ignores information that can be gained from previous iterations of the outer for loop
  - For example, if the smallest number + the largest number went over the target, we now know that we can ignore that
    largest number since it will go over the target for every other number.. since every other number is bigger than the
    smallest number
  - That example shows that there is information from every iteration that isn't used in this approach, since binary
    search is conducted over the entire array

  Time Complexity: O(NlogN)
  Space Complexity: O(1) -- using input as the output list
"""


def twoSum(self, numbers, target):
    l, r = 0, len(numbers) - 1
    while l < r:
        num = numbers[l] + numbers[r]
        if num == target:
            return [l + 1, r + 1]
        elif num < target:
            l += 1
        else:
            r -= 1

"""
  APPROACH #2: Two Pointers
  - Place a pointer on either end of the array
  - Add both values
    - If over the target, the largest can be ruled out, bring it down
    - If under the target, the smallest can be ruled out, bring it up
  
  - As the loop progresses, more and more of the extreme ends of the sorted array are ruled out until an exact match to
    the target is found
    
  - This approach, unlike Approach #1, takes advantage of the information available in the previous iteration
"""


def twoSum(self, numbers, target):
    ln = len(numbers)
    for id, num in enumerate(numbers):
        start = 0
        end = ln-1
        cur_tar = target-num
        while True:
            middle = int((start+end)/2)
            if numbers[middle] == cur_tar and middle != id:
                return [id+1, middle+1] if id < middle else [middle+1, id+1]
            if end <= start:
                break
            elif numbers[middle] < cur_tar:
                start = middle+1
            else:
                end = middle-1
