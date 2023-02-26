"""
  235. Lowest Common Ancestor of a Binary Search Tree
  [ Medium ] [ 61.2% ] -- Solved 25/02/2023 -- [ Binary Search Tree ]
  ----------------------------------------

  Problem:
  - Given a binary search tree with unique values, and two nodes, find the lowest common ancestor of the two nodes
  - Note: A node can be an ancestor of itself

  Approach:
  - Key idea: The lowest common ancestor of two nodes must be a node that has one of the target descendants in its left
    subtree, and one in its right subtree - there is no other way
    - Any node above would have both nodes in a single subtree, any node below would not have one or more of the
      target descendants as a descendant
  - Start from the root node, explore subtrees that have both of the target descendant nodes, the first node that has
    one target node in each subtree - that is the node that must be the lowest common ancestor

  Time Complexity: O(logN)
  Space Complexity; O(1)
"""


def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    if q.val < p.val:
        q, p = p, q
    while not p.val <= root.val <= q.val:
        root = root.left if p.val < root.val else root.right
    return root
