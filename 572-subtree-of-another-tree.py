"""
  211. Design Add and Search Words Data Structure
  [ Medium ] | [ 45.8% ] -- Solved 12/02/2023 -- [ DFS, Trie ]

  Problem Statement:
  - Self explanatory

  Approach:
  - Conduct DFS on the main tree, if the node being considers matches the root node of the subTree, check that the
    main tree has a subtree rooted at the current node that matches the target subtree
"""

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.subRoot = subRoot
        return self.dfs(root)

    def dfs(self, root):
        return ((root.val == self.subRoot.val) and self.checkMatch(root, self.subRoot)) or (
                    root.left and self.dfs(root.left)) or (root.right and self.dfs(root.right))

    def checkMatch(self, root, subRoot):
        if root is None and subRoot is None:
            return True
        if (root is None) or (subRoot is None):
            return False
        return (root.val == subRoot.val) \
               and self.checkMatch(root.left, subRoot.left) and self.checkMatch(root.right, subRoot.right)
