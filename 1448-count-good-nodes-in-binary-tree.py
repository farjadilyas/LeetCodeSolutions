"""
  1448. Count Good Nodes in Binary Tree
  [ Medium ] | [ 74.4% ] -- Solved 12/02/2023 -- [ BFS ]

  Problem Statement:
  - Good node definition: A node that has no node with a greater value in the path from the node to the root of the tree

  Approach:
  - Conduct DFS, keep track of the maximum value so far in the path, if the currennt node has a value that is >= the
    maximum so far, count it as a good node

  Time Complexity O(N)
  Space Complexity: O(H)
"""

def goodNodes(self, root: TreeNode) -> int:
    if not root:
        return 0
    return self.go(root, -10001)


def go(self, root, mx):
    res = 0
    if root.val >= mx:
        res = 1
        mx = root.val
    if root.left:
        res += self.go(root.left, mx)
    if root.right:
        res += self.go(root.right, mx)
    return res
