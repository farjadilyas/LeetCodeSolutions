"""
  133. Clone graph
  [ Medium ] | [ 57.0% ] -- Solved 9/04/2023 -- [ Array, DFS, BFS, Matrix, Union Find ]

  Problem Statement:
  - Given a reference of a node in a connected undirected graph
  - Return a deep copy (clone) of the graph
  - number of nodes < 100 - makes it worth it to use a boolean array instead of a hashmap to map original nodes to
    copied ones

  Approach:
  - DFS traversal, copy each node and map the original node to the cloned ones so that a given node can be linked to
    one that has already been clones

  Time Complexity: O(N)
  Space Complexity: O(N)
"""


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return None
        hm = [None for _ in range(101)]
        return self.recurse(node)

    def recurse(self, node):
        if self.hm[node.val] is not None: return self.hm[node.val]
        new_node = Node(node.val)
        self.hm[node.val] = new_node
        new_node.neighbors = [self.recurse(neighbor) for neighbor in node.neighbors]
        return new_node
