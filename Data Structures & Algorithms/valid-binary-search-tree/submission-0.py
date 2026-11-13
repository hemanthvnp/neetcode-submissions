# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        arr = []

        def inorder(node):
            if node is None:
                return

            inorder(node.left)
            arr.append(node.val)
            inorder(node.right)

        inorder(root)

        for i in range(1, len(arr)):
            if arr[i] <= arr[i-1]:
                return False

        return True