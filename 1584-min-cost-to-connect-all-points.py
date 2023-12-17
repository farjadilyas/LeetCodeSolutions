"""
  1584. Min Cost to Connect All Points
  [ Medium ] | [ 66.5% ] -- Solved 17/12/2023
  ----------- {{ SUBMISSION STATS }} --------------
  FASTER THAN: 84.2%
  MEMORY USAGE: 76.4%

  Problem:
  - Given a list of points on an x-y plane, where the cost to connect 2 points is the manhattan distance between them,
    find the minimum cost to connect all points
  - Manhattan distance -> block distance -> distance in x-dir + distance in y-dir

  Approach:
  - Very clearly need to find an MST
  - The graph is a dense one, E = V^2 since it is valid to go from any node to any node
  - Prim's MST is preferred for dense graphs
  - No need to actually create the adj list since we know that a node can go to every node

  Time Complexity: O(ElogE)
  Space Complexity: O(E)
"""


import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # format: (weight, index of node in points array)
        heap = [(0, 0)]
        num_points = len(points)
        visited = [False for _ in range(num_points)]
        num_visited = 0
        mst_weight = 0
        while heap and num_visited != num_points:
            weight, p_idx = heapq.heappop(heap)
            if visited[p_idx]:
                continue
            visited[p_idx] = True
            num_visited += 1
            mst_weight += weight
            for child_idx in range(num_points):
                if not visited[child_idx]:
                    heapq.heappush(heap, (abs(points[p_idx][0]-points[child_idx][0]) + abs(points[p_idx][1]-points[child_idx][1]), child_idx))
        return mst_weight
