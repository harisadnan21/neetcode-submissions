# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_index_map = {val: idx for idx, val in enumerate(inorder)}

        def build(pre_l, pre_r, in_l, in_r):
            if pre_l > pre_r or in_l > in_r:
                return None

            root_val = preorder[pre_l]
            root = TreeNode(root_val)
            root_inorder_idx = inorder_index_map[root_val]
            left_subtree_size = root_inorder_idx - in_l

            root.left = build(pre_l + 1, pre_l + left_subtree_size, in_l, root_inorder_idx - 1)
            root.right = build(pre_l + left_subtree_size + 1, pre_r, root_inorder_idx + 1, in_r)

            return root

        return build(0, len(preorder) - 1, 0, len(inorder) - 1)