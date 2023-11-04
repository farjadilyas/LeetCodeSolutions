class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        lr, lc = len(matrix), len(matrix[0])
        for ridx in range(lr):
            for cidx in range(lc):
                if matrix[ridx][cidx] != 0:
                    continue
                for zidx in range(lr):
                    if matrix[zidx][cidx] != 0:
                        matrix[zidx][cidx] = None
                for zidx in range(lc):
                    if matrix[ridx][zidx] != 0:
                        matrix[ridx][zidx] = None
        for ridx in range(lr):
            for cidx in range(lc):
                if matrix[ridx][cidx] is None:
                    matrix[ridx][cidx] = 0
        return matrix

        # 1 2 3 4
        # 5 0 7
