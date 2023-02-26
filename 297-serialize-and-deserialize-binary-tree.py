"""
  297. Serialize and Deserialize Binary Tree
  [ Hard ] | [ 55.3% ] -- Solved 26/02/2023 -- [ DFS, Binary Tree ]

  Problem Statement:
  - Given a binary tree, and its root::TreeNode, write methods to serialize and deserialize it to and from a string
    respectively

  Approach:
  - Key Idea:
    - Serialize: Use a preorder traversal and add a marker for every null child for a leaf node, use ',' for separating
      node values since they can be of multiple digits
    - Deserialize: Recursive preorder traversal while keeping track of the current index over the serialized string
      (preorder repr)
    - Eg: serialized: 3,9,:,:,20,15,:,:,7,:,:
    - The intuition is that since the nodes of a subtree are present in contiguous order, it is very easy to check
      if the left and right children are null, and go up a level in the recursion tree if they are
    - Dry run:
      - At every step, we move forward a step through the serialized repr
      - 3, 3left is 9, 9left is None, 9 right is None, 3right is 20, 20left is 15, 15left is None, 15right is None,
        7left is None, 7right is None
  - Returning the idx from a child is important since the parent knows the correct part of the preorder repr to resume
    its traversal from

  Time Complexity: O(N)
  Space Complexity: O(N)
"""

class Codec:
    def serialize(self, root):
        if not root:
            return ':'
        return str(root.val) + ',' + self.serialize(root.left) + ',' + self.serialize(root.right)

    def deserialize(self, data):
        self.des = data
        if data[0] == ':':
            return None
        self.limit = len(data)
        self.root = TreeNode()
        self.preorder(0, self.root)
        return self.root

    def preorder(self, idx, root):
        # second pointer to find the substring that contains the next potentially multi-digit node value
        eidx = idx
        while eidx < self.limit and self.des[eidx] != ',':
            eidx += 1
        root.val = int(self.des[idx:eidx])
        # Skip the ','
        idx = eidx + 1
        if idx < self.limit and self.des[idx] != ':':
            root.left = TreeNode()
            idx = self.preorder(idx, root.left)
        idx += 2
        if idx < self.limit and self.des[idx] != ':':
            root.right = TreeNode()
            idx = self.preorder(idx, root.right)
        return idx

class TreeNode(object):
    def __init__(self, x=None):
        self.val = x
        self.left = None
        self.right = None
