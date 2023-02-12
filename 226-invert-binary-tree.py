class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            self.invert(root)
        return root

    def invert(self, root):
        root.left, root.right = root.right, root.left
        if root.left:
            self.invert(root.left)
        if root.right:
            self.invert(root.right)
        return root