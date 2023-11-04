from typing import (
    List,
)

class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def valid_tree(self, n: int, edges: List[List[int]]) -> bool:
        parent = list(range(n))
        rank = [1] * n

        def find(node):
            cur = node
            while cur != parent[cur]:
                cur = parent[cur]
                parent[cur] = parent[parent[cur]]  # Path compression
            return cur

        # Union all nodes
        num_merges = 0
        for node1, node2 in edges:
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
            num_merges += 1
        return num_merges == n-1
