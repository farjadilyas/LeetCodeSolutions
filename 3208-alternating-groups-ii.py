def numberOfAlternatingGroups(colors: list[int], k: int) -> int:
    """
    Sliding window solution
    """
    N = len(colors)
    start = end = count = 0
    window_size = 1
    while start < N:
        while colors[(end+1) % N] != colors[end] and window_size < k:
            end = (end+1) % N
            window_size += 1
        # if window is maximized, shrink one step from start, to extend in next iter
        if window_size == k:
            count += 1
            start += 1
            window_size -= 1
        else:
            # end+1 is the element where the alternating sequence breaks, start new slide from here
            end = end+1
            # To make sure start doesn't go backwards (since we allow end to circle round)
            if end < start:
                break
            start = end
            window_size = 1
    return count


def numberOfAlternatingGroupsSimle(colors: list[int], k: int) -> int:
    """
    DP-like solution
    """
    count, N = 1, len(colors)
    result = 0
    # Alt groups in circle, so first and last are next to each other
    # Hence, the farthest the window can go without getting a duplicate window is starting at the last element and
    # ending at the N+k-2 element -> N-1 + k - 1 (the second -1 prevents steps back from the duplicate window)
    # So go from 1..N+k-2 and maintain a running count of flips, reset the count if a flip doesn't happen
    # If the running count goes >= k, that means you're in a window of k alternating elements
    for i in range(1, len(colors)+k-1):
        count = 1 if colors[(i-1) % N] == colors[i % N] else count + 1
        result += count >= k
    return result
