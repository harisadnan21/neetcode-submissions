# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # preorder = [1,2,3,4], 
        #  inorder = [2,1,3,4]
        if not preorder and not inorder:
            return None
            

        newNode = TreeNode()
        newNode.val = preorder[0]
        inorder_idx = inorder.index(preorder[0])

        newNode.left = self.buildTree(preorder[1:1 + inorder_idx] ,inorder[:inorder_idx])
        newNode.right = self.buildTree( preorder[1 + inorder_idx: ], inorder[inorder_idx + 1:])
        return newNode





            
        


        