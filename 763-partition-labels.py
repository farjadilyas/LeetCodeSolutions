class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # ababcbacadefegdehijhklij
        # a: 0, 8
        # b: 1, 5
        # c: 4, 7
        # d: 9, 14
        # e: 10, 15

        hm = [None for _ in range(26)]
        for idx, c in enumerate(s):
            cidx = ord(c)-97
            if not hm[cidx]:
                hm[cidx] = [idx, idx]
            else:
                hm[cidx][1] = idx
        intervals = [e for e in hm if e]
        intervals.sort()
        current_interval = intervals[0]
        merged_intervals = []
        for i in range(1, len(intervals)):
            if not intervals[i]:
                continue
            if max(current_interval[0], intervals[i][0]) > min(current_interval[1], intervals[i][1]):
                merged_intervals.append(current_interval[1]-current_interval[0]+1)
                current_interval = intervals[i]
            else:
                current_interval[0] = min(current_interval[0], intervals[i][0])
                current_interval[1] = max(current_interval[1], intervals[i][1])
        merged_intervals.append(current_interval[1]-current_interval[0]+1)
        return merged_intervals
