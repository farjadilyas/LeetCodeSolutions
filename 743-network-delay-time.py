"""
  743. Network Delay Time
  [ Medium ] | [ 53.1% ] -- Solved 17/12/2023
  ----------- {{ SUBMISSION STATS }} --------------
  FASTER THAN: 98.4%
  MEMORY USAGE: 95.5%

  Problem:
  - Given a network of edges with the travel times between them, the number of nodes, and a source node k
  - Find the minimum time for a signal to reach all nodes
  - If it can't reach all nodes, return -1

  Approach:
  - Clearly a single-source shortest path problem
  - The destination node with the longest shortest path - that path weight is the answer
  - Use Dijkstra's algo
  - If a node remains unvisited - return -1
  - Could also use Union Find while building the adj list to return early if the network has more than 1 connected
    component

  Time Complexity: O(ElogE)
  Space Complexity: O(E)
"""


from collections import defaultdict
import heapq


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for edge in times:
            graph[edge[0]].append(edge)
        weights = [10_000_000 for _ in range(n + 1)]
        visited = [False for _ in range(n + 1)]
        weights[0] = weights[k] = 0
        heap = [(0, k, k)]
        while heap:
            edge_weight, source_node, node = heapq.heappop(heap)
            if visited[node]:
                continue
            visited[node] = True
            weights[node] = edge_weight
            for child in graph[node]:
                if not visited[child[1]] and edge_weight + child[2] < weights[child[1]]:
                    weights[child[1]] = edge_weight + child[2]
                    heapq.heappush(heap, (edge_weight + child[2], child[0], child[1]))
        max_weight = max(weights)
        return max_weight if max_weight < 10_000_000 else -1
