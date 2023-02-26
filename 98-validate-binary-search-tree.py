"""
  98. Validate Binary Search Tree
  [ Medium ] | [ 31.9% ] -- Solved 25/02/2023 -- [ DFS, BST ]

  Problem Statement:
  - Self explanatory - subtrees must be less than and greater than, not equal to

  Approach:
  - Conduct an inorder traversal to view the nodes in a sorted order
  - Store the value of the last viewed node - since nodes are being traversed in order, no new node should be <= the
    previous' value for the BST to be valid

  Time Complexity: O(N)
  Space Complexity: O(H)
"""

def isValidBST(self, root: Optional[TreeNode]) -> bool:
    self.cur = (-2 ** 31) - 1
    return self.inorder(root)


def inorder(self, root):
    res = True
    if root.left:
        res = res and self.inorder(root.left)
    if not res or root.val <= self.cur:
        return False
    self.cur = root.val
    if root.right:
        res = res and self.inorder(root.right)
    return res
