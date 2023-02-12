class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.inorder(root, 1) if root else 0

    def inorder(self, root, depth):
        return max(
            self.inorder(root.left, depth + 1) if root.left else depth,
            self.inorder(root.right, depth + 1) if root.right else depth,
        )