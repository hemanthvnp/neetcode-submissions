class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        maxcount = 0

        def finddepth(root):
            nonlocal maxcount

            if root is None:
                return 0

            left = finddepth(root.left)
            right = finddepth(root.right)

            maxcount = max(maxcount, left + right)

            return 1 + max(left, right)

        finddepth(root)
        return maxcount