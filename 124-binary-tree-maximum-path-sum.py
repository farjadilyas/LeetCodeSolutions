"""
  124. Binary Tree Maximum Path Sum
  [ Hard ] | [ 39.2% ] -- Solved 26/02/2023 -- [ DFS, Tree, Dynamic Programming ]

  Problem Statement:
  - Path sum: Sum of values of all nodes along a path between any two nodes in the tree - find it
  - Nodes can have negative values - [-1000, 1000]

  Approach:
  - Conduct a postorder traversal
  - Key ideas:
    - Any path must have a root node for which all other nodes are descendants
    - The max path does not necessarily go through the root of the entire tree
    - For each root node, the max path with that root node either involves some combination of the left and right
      paths with the value of the current node - cur, left+cur, right+cur, left+right+cur
      - This is because nodes can have negative values - so we want to be able to not add sub paths with negative values
    - Imp point: The current root might be a subtree, the only restriction for this case is that we can't add both
      the left and right sum, since they link to two nodes already, so we'll pick max(left,right,0)+cur

  Time Complexity: O(N)
  Space Complexity: O(H)
"""

def maxPathSum(self, root: Optional[TreeNode]) -> int:
    self.mx = -1001
    self.postorder(root)
    return self.mx

def postorder(self, root):
    leftSum = rightSum = -1001
    if root.left:
        leftSum = self.postorder(root.left)
    if root.right:
        rightSum = self.postorder(root.right)
    self.mx = max(self.mx, max(leftSum, rightSum, leftSum + rightSum, 0) + root.val)
    return max(leftSum, rightSum, 0) + root.val
