# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.retval = float('-inf')

        def rec(node):
            if not node:
                return 0
            recleft = max(0, rec(node.left))
            recright= max(0, rec(node.right))
            maxval = recleft + recright + node.val
            self.retval = max(self.retval, maxval)
            return max(node.val + recleft, node.val + recright)
        rec(root)
        return self.retval

        