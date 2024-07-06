def rotate(nums: list[int], k: int) -> None:
    """
    - Create a temp array of size k, store the last k elements in it
    - Move the first len-k elements k steps forward
    - Copy the temp array into the first k elements
    Time complexity: O(N)
    Space Complexity: O(k)
    """
    k = k % len(nums)
    tmp = [nums[-k + i] for i in range(k)]
    for i in range(len(nums) - k - 1, -1, -1):
        nums[i + k] = nums[i]
    for i in range(k):
        nums[i] = tmp[i]


def rotate_optimal(nums: list[int], k: int) -> None:
    """
    Conceptually break down array in to 2 pieces a,b like [--a--, --b--] where --b-- is of length k%len(nums)
    After k right-rotations, note that the array will look like [--b--, --a--]
    - Also note that after reversing the original array, the array looks like [reversed(--b--), reversed(--a--)]
    - So: reverse the full array, then reverse the subarray containing the first k elements, then reverse the subarray
      containing the remaining elements to arrive at [--b--, --a--], and hence, the answer
    Time Complexity: O(N)
    Space Complexity: O(1)
    """
    k = k % len(nums)
    for i in range(len(nums) // 2):
        nums[i], nums[-i-1] = nums[-i-1], nums[i]
    for i in range(k // 2):
        nums[i], nums[k - i - 1] = nums[k - i - 1], nums[i]
    for i in range((len(nums) - k) // 2):
        nums[k + i], nums[-i - 1] = nums[-i - 1], nums[k + i]
