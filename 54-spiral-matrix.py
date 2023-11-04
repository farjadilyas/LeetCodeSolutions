
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        lm, ln = len(matrix), len(matrix[0])
        # create direction arrays of the format [row_offset, col_offset, next_direction]
        # its imp that next_direction is a _pointer_ to another direction array
        # start with right till you meet the end of the arr or a visited element,
        # then set current direction to next_direction
        up = [-1, 0, None]
        left = [0, -1, up]
        down = [1, 0, left]
        cd = right = [0, 1, down]
        up[2] = right
        blocked_sides = cr = cc = 0
        ret = [matrix[0][0]]
        matrix[0][0] = None
        # If elements in all directions have been visited, break out of the loop
        while blocked_sides != 4:
            nr, nc = cr+cd[0], cc+cd[1]
            if 0 <= nr < lm and 0 <= nc < ln and matrix[nr][nc] is not None:
                cr, cc = nr, nc
                ret.append(matrix[cr][cc])
                matrix[cr][cc] = None
                blocked_sides = 0
            else:
                cd = cd[2]
                blocked_sides += 1
        return ret
