# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
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
        rightside = []
        for i in range(len(res)):
            rightside.append(res[i][-1])
        return rightside
        