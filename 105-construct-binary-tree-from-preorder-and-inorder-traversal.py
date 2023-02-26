"""
  105. Construct Binary Tree from Preorder and Inorder Traversal
  [ Medium ] | [ 61.3% ] -- Solved 26/02/2023 -- [ Divide and Conquer, Hash Table, Binary Tree ]

  Problem Statement:
  - Self explanatory - all elements are unique, min # nodes = 1

  Foundation:
  - This is a pretty tricky problem... Need to realise what information each type of traversal gives you
  - Preorder traversal has each and every subtree in a cluster in the given array
    - eg: [3, 9, 20, 15, 7] - leetcode example - here, [9], [20,15,7] can be the subtrees, or maybe [9,20],[15,7] -
      whatever it is, *the elements for a subtree will be contiguously present in the array*
  - Inorder traversal has the property that for any element in the array, the nodes to its left will be in its left
    subtree, and the nodes to its right will be in its right subtree
  - We have to combine this information to form a Binary Tree

  Thought process for arriving at approach:
  - Implement a recursive preorder traversal, using the elements in the preorder traversal array
  - Use the inorder traversal array to guide the preorder traversal, i.e, to check what paths are valid
  - Example: preorder: [3,9,20,15,7] - Here, 9 and 20 may be children of 3, or 3 may only have 9 as its only child,
    and 20 and 15 might be 9's children
  - Basically, we know nodes of a subtrees are contiguous in the preorder array, but we don't know how to identify
    whether a node is in a particular subtree
  - Idea: It is very easy to check whether a node is in a particular subtree given the root, using the inorder array

  - Build a hashmap of element: index using the inorder array
  - During the preorder traversal, if we are going to explore the left subtree, we must check that for the next element
    in the preorder traversal - its index in the inorder traversal array is less than that of the root, i.e, for
    the next node in the preorder traversal to be in the left subtree, it must occur to the left of the root node in
    the inorder traversal

  - Additional Constraint: We also need to be mindful of the fact that the inorder array tells us how many elements
    are in the left and right subtree since the root splits the array into two subtrees
  - Example on why this is important - preorder:[3,9,20,15], inorder: [9,3,15,20,7]
    - during preorder traversal when we reach 20, and are traversing the right subtree of 9, we can't just check that
      20 occurs to the right of 9 in the inorder array  - it must occur to the right of 9 AND to the left of 3 to be
      a descendant of 9 and 3, and for us to put it as the right child of 9
  - Implementing this: for every step of the traversal, maintain a min and max index the node must confirm to WITH
    RESPECT TO THE INORDER ARRAY
  - Essentially maintain a window over the inorder array that represents the nodes that are valid for this stage of the
    preorder traversal, so during the preorder traversal, we can only traverse the nodes that occur in the current valid
    inorder window

  - Implementation detail: The recursive preorder implementation will naturally iterate over the preorder array ...
    since the traversal is in the same order
  - So it's easy to keep track of how far along we are the preorder array
  - Maintain a current index (cidx), increment it whenever a node has found its place, and return it so that parent
    nodes know where to resume from once their children have done their part in building the tree


  Simpler way of thinking about approach:
  - Build a element: index hashmap using the inorder array
  - Implement recursive preorder traversal to effectively iterate over the preorder array
  - At every step in the traversal, pick the current node as the root
  - Use the inorder hashmap to get the index of the current root - this effectively splits the inorder array into two
    subtrees and allows for fast checking of whether any node is in a given subtree
  - We keep track of the inorder subtree being considered using min max index on the inorder array, the current node's
    index in the inorder array serves the purpose of further narrowing the inorder window when we go on to traverse the
    left and right subtrees of this node
  - Summary: Build a hashmap of the inorder array to support fast subtree membership checking, conduct a preorder
    traversal and add each node that satisfies the expected inorder subtree membership for the current preorder
    traversal step

  Time Complexity: O(N)
  Space Complexity: O(H)
"""

def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    self.hm = {e: i for i, e in enumerate(inorder)}
    self.preorder = preorder
    self.limit = len(preorder)
    root = TreeNode()
    self.do_preorder(0, 0, -1, self.limit, root)
    return root

def do_preorder(self, cidx, ridx, mn, mx, root):
    cur = self.preorder[cidx]
    root.val = cur
    inorder_idx = self.hm[cur]
    # Consider the next node in the preorder traversal, gets its inorder index and check that it is within the expected
    # inorder window
    # We constrict the window in this step - if we are stepping into the left subtree, the max inorder index will be
    # reduced - opposite for stepping into the right subtree
    if cidx + 1 < self.limit and mn < self.hm[self.preorder[cidx + 1]] < min(mx, inorder_idx):
        child = self.preorder[cidx + 1]
        if self.hm[child] < inorder_idx:
            root.left = TreeNode()
            cidx = self.do_preorder(cidx + 1, 1 + (2 * ridx), mn, min(mx, inorder_idx), root.left)

    if cidx + 1 < self.limit and max(mn, inorder_idx) < self.hm[self.preorder[cidx + 1]] < mx:
        child = self.preorder[cidx + 1]
        if self.hm[child] > inorder_idx:
            root.right = TreeNode()
            cidx = self.do_preorder(cidx + 1, 2 + (2 * ridx), max(mn, inorder_idx), mx, root.right)
    return cidx

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
