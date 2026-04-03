# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, maxTillNow):
            if not node:
                return 0
            if node.val >= maxTillNow:
                # is a good node
                maxTillNow = node.val 
                return dfs(node.left, maxTillNow) + dfs(node.right, maxTillNow) + 1 

            else:
                return dfs(node.left, maxTillNow) + dfs(node.right, maxTillNow)
        return dfs(root, float("-inf"))

        