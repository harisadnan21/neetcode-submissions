# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int: 
        self.ret = 0
        def recurse(n):
            if not n: 
                return
            if not n.left and not n.right:
                n.val = 0
            elif not n.left:
                recurse(n.right)
                n.val = 1 +n.right.val
                self.ret = max(self.ret, n.val)
            elif not n.right:
                recurse(n.left)
                n.val = 1 + n.left.val
                self.ret = max(self.ret, n.val)
            else:
                recurse(n.left)
                recurse(n.right)
                n.val = max(n.left.val, n.right.val) + 1
                self.ret = max(self.ret, n.left.val + n.right.val + 2 )
        recurse(root)
        return self.ret

        