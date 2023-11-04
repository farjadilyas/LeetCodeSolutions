from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        # {1: 1, 2: 2, 3: 2, 4: 1, 6: 1, 7: 1, 8: 1}
        hm = Counter(hand)
        groups = 0
        for start in sorted(hm.keys()):
            span_length = hm[start]
            if span_length == 0:
                continue
            groups += span_length
            for current in range(start+1, start+groupSize):
                if current not in hm or hm[current] < span_length:
                    return False
                hm[current] -= span_length
        return groups

        # [1, 2, 2, 3, 3, 4, 6, 7, 8]
        # 1->2->3
        # 2->3->4
        # 6->7->8
        # {
        #     3: [2]
        # }
        # ...
