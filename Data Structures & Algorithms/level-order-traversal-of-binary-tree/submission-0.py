class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        def levelorder(root, level):
            if root is None:
                return

            if level == len(res):
                res.append([])

            res[level].append(root.val)

            levelorder(root.left, level + 1)
            levelorder(root.right, level + 1)

        levelorder(root, 0)
        return res