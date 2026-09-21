# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        lTree =1
        rTree=1
        if root.left != None:
            lTree = self.maxDepth(root.left) + 1
        if root.right != None:
            rTree = self.maxDepth(root.right)+1
        return max(lTree,rTree)
        