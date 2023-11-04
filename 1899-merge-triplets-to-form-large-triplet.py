class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        result = [0, 0, 0]
        for triplet in triplets:
            any_match = False
            for i in range(3):
                if triplet[i] > target[i]:
                    any_match = False
                    break
                if not any_match and triplet[i] == target[i]:
                    any_match = True
            if not any_match:
                continue
            all_match = True
            for i in range(3):
                if triplet[i] > result[i]:
                    result[i] = triplet[i]
                if all_match and result[i] != target[i]:
                    all_match = False
            if all_match:
                return True
        return False
