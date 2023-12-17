"""
  778. Swim in Raising Water
  [ Hard ] | [ 60.3% ] -- Solved 17/12/2023
  ----------- {{ SUBMISSION STATS }} --------------
  FASTER THAN: 47.6%
  MEMORY USAGE: 36.0%

  Problem:
  - Given a grid of tiles, and their elevations
  - Picture a scenario where as time t increments, the water level increases by 1
  - You can move in 4 directions from a given square, only to a square that has the same elevation
    - Here, elevation is max(elevation of tile, time t that has passed)
  - If you start on coordinates 0,0, find the minimum time in which you can reach the (n-1, n-1) tile (bottom-right)

  Approach:
  - Can think of this as a flooding problem
  - As time passes, more nodes become eligible to be connected
  - Seems like a job for the Union-Find data structure

  - 1 <= n <= 50 and 0 <= grid[i][j] <= n^2
  - So max elevation: 250, max num tiles: 250
  - At worst answer will be 250
  - We can either go from t=1 to t-250, or (better) we can sort the tiles by their elevations (nlogn)
  - Iterate over the tiles in sorted order, union the tile with the surrounding tiles whose elevations are lower
  - After each iteration we can find() whether the parent of the start and end are the same, if so, the
    start becomes connected to the end at time = elevation of current tile, because before this tile was introduced to
    our network, the source and dest were unconnected
  - Doing this in sorted order means that we find the minimum time

  Time Complexity: O(N^2logN)
  - Sorting cost: nxn grid, n^2 cells, sorting: N^2 log(N^2) -> N^2 logN
  - Union-Find cost: worst case: N^2logN, amortized: N^2
  Space Complexity: O(N)
"""


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        elevations = [(cell, r_id, c_id) for r_id, row in enumerate(grid) for c_id, cell in enumerate(row)]
        elevations.sort()
        n = len(grid)
        nsq = n ** 2
        parents = [i for i in range(nsq)]
        rank = [1 for _ in range(nsq)]

        def find(e):
            while parents[e] != e:
                # CAUTION! In chained assignments..
                # The rightmost value is evaluated, then the assignment happens left-to right
                # So if you write this: e = parents[e] = parents[parents[e]]...
                # It will be e = parents[parents[e]] and parents[e] = e
                # This will mean that the tree rooted at parents[e] will now be SEPARATED from the rest
                # the correct assignment would be parents[e] = e = parents[parents[e]]
                # or more simply
                parents[e] = parents[parents[e]]
                e = parents[e]
            return e

        def union(n1, n2):
            pn1, pn2 = (find(n1), find(n2)) if rank[n1] > rank[n2] else (find(n2), find(n1))
            if pn1 != pn2:
                parents[pn2] = parents[pn1]
                rank[n1] += rank[n2]

        for i in range(1, len(elevations)):
            # Merge current cell with its neighbours if possible
            cell, r_id, c_id = elevations[i]
            if r_id - 1 >= 0 and cell > grid[r_id - 1][c_id]:
                union((n * r_id) + c_id, n * (r_id - 1) + c_id)
            if c_id - 1 >= 0 and cell > grid[r_id][c_id - 1]:
                union((n * r_id) + c_id, n * (r_id) + c_id - 1)
            if r_id + 1 < n and cell > grid[r_id + 1][c_id]:
                union((n * r_id) + c_id, n * (r_id + 1) + c_id)
            if c_id + 1 < n and cell > grid[r_id][c_id + 1]:
                union((n * r_id) + c_id, n * (r_id) + c_id + 1)
            # Check if the source and sink are now connected
            if find(0) == find(nsq - 1):
                return cell
        return elevations[-1][0]

