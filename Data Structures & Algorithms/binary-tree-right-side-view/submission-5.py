# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # tree traversal,
        #add val
        # right
        # left
        #add only when the height is > max
        self.lst = []
        self.maxHeight = float('-inf')

        def recurse(node , currHeight):

            if not node:
                return
            print(node.val, currHeight)
            if currHeight > self.maxHeight:
                self.lst.append(node.val)
                self.maxHeight = currHeight

            recurse(node.right, currHeight + 1)
            recurse(node.left, currHeight + 1)


        recurse(root, 0)
        return self.lst



        