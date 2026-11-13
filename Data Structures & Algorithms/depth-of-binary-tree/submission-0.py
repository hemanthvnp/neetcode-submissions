# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        maxcount=0
        count=1
        def finddepth(root,count):
            if root==None:
                return
            if root.left==None and root.right==None:
                nonlocal maxcount
                maxcount = max(count,maxcount)
                count = 1
                return
            if root.left:
                finddepth(root.left,count+1)
            if root.right:
                finddepth(root.right,count+1)
        finddepth(root,count)
        return maxcount
            
        