"""
  3651. Number of connected components in an undirected graph
  [ Medium ] | [ 39.3% ] -- Solved 04/11/2023 -- [ Graph, Union Find ]
  ---------- {{ SUBMISSION STATS }} ---------------
  FASTER THAN: 99.35%
  MEMORY USAGE: 97.85%

  Problem:
    - In this problem, there is an undirected graph with n nodes
    - There is also an edges array. Where edges[i] = [a, b] means that there is an edge between
      node a and node b in the graph
    - You need to return the number of connected components in that graph.

  Approach:
  - Example scenario: [1,2,3,4], [5,6], [7,8], [9] - each list is a connected component, where the nodes within
    are connected - Answer here is: 4
  - Classic Union Find problem - start with 9 unmerged nodes, iterate through edges and merge nodes
  - Count the number of merges (don't count a union as a merge if they were already in the same component)
  - Number of nodes - Number of merges = Number of connected components
"""


from typing import (
    List,
)


class Solution:
    """
    @param n: the number of vertices
    @param edges: the edges of undirected graph
    @return: the number of connected components
    """

    def count_components(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))
        rank = [1] * n

        def find(node):
            cur = node
            while cur != parent[cur]:
                cur = parent[cur]
                parent[cur] = parent[parent[cur]]  # Path compression
            return cur

        def union(node1, node2):
            if node1 == node2:
                return False
            node1_parent = find(node1)
            node2_parent = find(node2)
            if node1_parent == node2_parent:
                return False
            if rank[node2] > rank[node1]:
                node1, node2, node1_parent, node2_parent = node2, node1, node2_parent, node1_parent
            # By here: node1 is the bigger one
            parent[node2_parent] = node1_parent
            rank[node1_parent] += rank[node2_parent]
            return True

        return n - sum(union(edge[0], edge[1]) for edge in edges)
