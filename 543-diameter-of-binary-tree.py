"""
  543. Diameter of Binary Tree
  [ Easy ] | [ 56.6% ] -- Solved 19/02/2023 -- [ Binary Tree, DFS ]

  Problem Statement:
  - Return the length of the diameter of a binary tree
  - This is the longest path between any two nodes of the tree, and does not necessarily involve the root

  Approach:
  - Property: For a given node, depth of subtree with root=node.left + depth of subtree with root=node.right =
    diameter of the subtree with root=node
  - Every node needs to return the depth of its SUBTREE (so leaf node has depth 0), along with the diameter of
    its subtree
  - Can do DFS, and maintain the depth and diameter while backtracking
  - Depth needs to be returned to calculate diameter for the parent node, diameter needs to be returned since the
    max diameter may involve any subtree

  Time Complexity: O(N)
"""

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root)[1]

    def dfs(self, root):
        left = self.dfs(root.left) if root.left else (0, 0)
        right = self.dfs(root.right) if root.right else (0, 0)
        return max(left[0]+1, right[0]+1), max(left[0]+right[0], left[1], right[1])
