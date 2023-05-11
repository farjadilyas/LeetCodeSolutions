

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        lx, ly, ret = len(heights), len(heights[0]), []

        def recurse(x, y, visited, prevHeight):
            if x < 0 or y < 0 or x == lx or y == ly or visited[x][y] or heights[x][y] < prevHeight:
                return
            visited[x][y] = True
            recurse(x + 1, y, visited, heights[x][y])
            recurse(x, y + 1, visited, heights[x][y])
            recurse(x - 1, y, visited, heights[x][y])
            recurse(x, y - 1, visited, heights[x][y])

        visitedPacific = [[False for y in range(ly)] for x in range(lx)]
        visitedAtlantic = [[False for y in range(ly)] for x in range(lx)]
        for xidx in range(lx):
            recurse(xidx, 0, visitedPacific, heights[xidx][0])
            recurse(xidx, ly - 1, visitedAtlantic, heights[xidx][ly - 1])
        for yidx in range(ly):
            recurse(0, yidx, visitedPacific, heights[0][yidx])
            recurse(lx - 1, yidx, visitedAtlantic, heights[lx - 1][yidx])
        for xidx in range(lx):
            for yidx in range(ly):
                if visitedPacific[xidx][yidx] and visitedAtlantic[xidx][yidx]:
                    ret.append([xidx, yidx])
        return ret
