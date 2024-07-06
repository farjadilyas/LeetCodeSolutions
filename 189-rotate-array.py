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


def rotate_optimal_reversed(nums: list[int], k: int) -> None:
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


def rotate_optimal_cyclic_replacements(nums: list[int], k: int) -> None:
    """
    - This approach places each element in its desired place one by one.
    - If you place one element in its desired place, it displaces the next element
    - So place that element in its desired place and so on
    - If this 'cyclic replacement' breaks (if n%k==0, see e.g. below), then move a step forward and continue the cyclic
      replacements
    """
    size = len(nums)
    k = k % size
    start = count = 0
    # count tracks how many elements have been put in their final desired place
    while count < size:
        # current set to the start of the new run
        current = start
        prev = nums[current]
        while True:
            # move current to the index where prev should be
            current = (current+k) % size
            temp = nums[current]
            nums[current] = prev
            prev = temp
            count += 1
            if current == start:
                # Happens when n%k == 0 (otherwise one outer loop will take the count to N)
                # at this point the inner loop has replaced n/k elements
                # so move current to the right by 1 and start again
                # eg: [1,2,3,4] k=2 - after one inner loop: [3,2,1,4], current === start == 0
                # so current = start + 1, after another loop: [3,4,1,2] (the answer)
                start += 1
                break
