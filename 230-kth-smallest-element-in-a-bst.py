"""
  230. Kth Smaller Element in a BST
  [ Medium ] | [ 70.0% ] -- Solved 25/02/2023 -- [ DFS, BST ]

  Problem Statement:
  - Self explanatory

  Approach:
  - Conduct an inorder traversal to view the nodes in a sorted order
  - Maintain the answer and count of nodes seen on the class level for efficiency and simplicity

  Time Complexity: O(N)
  Space Complexity: O(H)
"""

def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    self.cur, self.k, self.ans = 1, k, None
    self.inorder(root)
    return self.ans


def inorder(self, root):
    if root.left:
        self.inorder(root.left)
    if self.cur == self.k:
        self.ans = root.val
    self.cur += 1
    if self.ans is None and root.right:
        self.inorder(root.right)
