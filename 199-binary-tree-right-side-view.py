"""
  199. Binary Tree Right Side View
  [ Medium ] | [ 61.5% ] -- Solved 25/02/2023 -- [ DFS, Trie ]

  Problem Statement:
  - Self explanatory

  Approach:
  - Conduct DFS on the main tree, if the node being considers matches the root node of the subTree, check that the
    main tree has a subtree rooted at the current node that matches the target subtree
"""

def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []
    queue = deque()
    queue.append(root)
    queue.append(None)
    ret = []
    cret = None
    while True:
        e = queue.popleft()
        if not queue:
            if cret is not None:
                ret.append(cret)
            return ret
        if e is None:
            if cret is not None:
                ret.append(cret)
            cret = None
            queue.append(None)
            continue
        if e.left:
            queue.append(e.left)
        if e.right:
            queue.append(e.right)
        cret = e.val