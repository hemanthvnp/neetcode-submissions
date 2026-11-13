class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def height(root):
            if root is None:
                return 0

            left = height(root.left)
            right = height(root.right)

            return 1 + max(left, right)

        if root is None:
            return True

        left = height(root.left)
        right = height(root.right)

        if abs(left - right) > 1:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)