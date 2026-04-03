# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #breadth first search
        # use a queue
        # 2 , 3 
        q = []
        retlst= []
        level = 0
        q.append(root)
        while q:
            levellst = []
            qlen = len(q)
            for nodeIdx in range(qlen):
                a = q.pop(0)
                #each a is a node on this level
                if not a:
                    continue

                levellst.append(a.val)
                q.append(a.left)
                q.append(a.right)
            retlst.append(levellst) if levellst else None


            
        # for loop


        return retlst
        