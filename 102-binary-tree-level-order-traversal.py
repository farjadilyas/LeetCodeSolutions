"""
  102. Binary Tree Level Order Traversal
  [ Medium ] [ 64.1% ] -- Solved 25/02/2023 -- [ Binary Tree, Breadth First Search ]
  ----------------------------------------

  Problem:
  - Given a binary tree, return a list, where each sublist is a level, and its items are the nodes on that level of
    the tree, ordered from left to right

  Approach:
  - Simple breadth first search
  - Used None as a marker to mark the end of a sequence of nodes that belonged to a single level
  - Could also have used the sie of the queue at the end of a level to achieve the same effect required to make
    sublists for each level

  Time Complexity: O(N)
  Space Complexity; O(N)
"""

from collections import deque
def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []
    queue = deque()
    queue.append(root)
    queue.append(None)
    ret = []
    cret = []
    while True:
        e = queue.popleft()
        if not queue:
            ret.append(cret)
            return ret
        if e is None:
            ret.append(cret)
            cret = []
            queue.append(None)
            continue
        if e.left:
            queue.append(e.left)
        if e.right:
            queue.append(e.right)
        cret.append(e.val)
