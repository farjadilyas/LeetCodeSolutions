"""
  110. Balanced Binary Tree
  [ Easy ] | [ 48.8% ] -- Solved 19/02/2023 -- [ Binary Tree, DFS ]

  Problem Statement:
  - Determine if the given binary tree is height-balanced
  - Height-balanced: If the depth of the two subtrees of every node does not differ by more than one

  Approach:
  - DFS, backtrack and return depth - but if the depth of the left and right subtree differs by more than 1, then
    return None
  - Whenever a parent node receives None from either one of its subtrees, it propagates it upwards towards the root
"""

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root) if root else True

    def dfs(self, root):
        left = self.dfs(root.left) if root.left else 0
        right = self.dfs(root.right) if root.right else 0
        return max(left + 1, right + 1) if left is not None and right is not None and abs(right - left) <= 1 else None
