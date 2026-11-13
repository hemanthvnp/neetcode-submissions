class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def sametree(p, q):
            if p is None and q is None:
                return True

            if p is None or q is None:
                return False

            if p.val != q.val:
                return False

            return sametree(p.left, q.left) and sametree(p.right, q.right)

        def findtree(root, subRoot):
            if root is None:
                return False

            if root.val == subRoot.val:
                if sametree(root, subRoot):
                    return True

            return findtree(root.left, subRoot) or findtree(root.right, subRoot)

        if subRoot is None:
            return True

        if root is None:
            return False

        return findtree(root, subRoot)