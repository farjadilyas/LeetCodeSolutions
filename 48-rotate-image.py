class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        lm = len(matrix)
        # center describes how close you're getting to the center
        # 0 is furthest out, lm//2-1 is one layer around the center (even odd cases)
        # cursor tracks how far along we are on each side's fixed span
        for center in range(lm//2):
            for cursor in range(center, lm-1-center):
                """
                top-side -> matrix[center][cursor]
                right-side -> matrix[cursor][lm-center-1]
                bottom-side -> matrix[lm-center-1][lm-cursor-1]
                left-side -> matrix[lm-cursor-1][center]

                algo:
                tmp = right-side
                right-side = top-side
                tmp2 = bottom-side
                bottom-side = tmp
                tmp = left-side
                left-side = tmp2
                top-side = tmp
                """
                tmp = matrix[cursor][lm-center-1]
                matrix[cursor][lm-center-1] = matrix[center][cursor]
                tmp2 = matrix[lm-center-1][lm-cursor-1]
                matrix[lm-center-1][lm-cursor-1] = tmp
                tmp = matrix[lm-cursor-1][center]
                matrix[lm-cursor-1][center] = tmp2
                matrix[center][cursor] = tmp

        return matrix