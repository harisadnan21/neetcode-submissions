# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.lst = []
        def collectToLst(root):
            if not root:
                return
            collectToLst(root.left)
            self.lst.append(root.val)
            collectToLst(root.right)

        collectToLst(root)
        return self.lst[k-1]

        