# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return "N"
        return str(root.val) +"," + self.serialize(root.left) + "," + self.serialize(root.right)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        print(data)
        lst = data.split(",")
        self.i=0 
        def deser():
            if lst[self.i] == "N":
                self.i +=1
                return None
            root = TreeNode(int(lst[self.i]))
            self.i +=1
            root.left = deser()
            root.right= deser()
            return root
        return deser()

