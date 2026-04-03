# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # for each node, find the distance of node on right from leaf, 
        self.saveHeight(root)
        return self.answerHelper(root)
            
    def answerHelper(self, root):
        if not root:
            return True
        if not root.left and not root.right:
            return True
        if not root.right:
            return root.left.val < 1

        if not root.left:
            return root.right.val < 1

        return self.answerHelper(root.left) and self.answerHelper(root.right) and (abs(root.left.val - root.right.val) < 2)


    
    def saveHeight(self, node):
        if not node:
            return
        if not node.left and not node.right:
            node.val = 0
            return
        if not node.right:
            self.saveHeight(node.left)
            node.val = node.left.val + 1
            return 
        if not node.left:
            self.saveHeight(node.right)
            node.val = node.right.val + 1
            return
        self.saveHeight(node.right)
        self.saveHeight(node.left)  
        node.val = max(node.right.val, node.left.val) + 1
        return 


        



        


        