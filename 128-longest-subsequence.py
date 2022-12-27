def longestConsecutive(self, nums: List[int]) -> int:
    hs = set()
    for num in nums:
        hs.add(num)

    mx = 0
    for k in hs:
        if k - 1 not in hs:
            cur = k + 1
            curx = 1
            while cur in hs:
                cur += 1
                curx += 1
            mx = max(mx, curx)
    return mx