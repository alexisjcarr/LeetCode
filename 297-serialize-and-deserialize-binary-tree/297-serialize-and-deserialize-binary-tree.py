# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

NONE = "None"

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def dfs(root, encoded=""):
            if not root:
                encoded += f"{NONE} "
            
            else:
                encoded += f"{str(root.val)} " 
                encoded = dfs(root.left, encoded)
                encoded = dfs(root.right, encoded)

            return encoded
            
        return dfs(root)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        encoded = data.split(" ")

        def dfs(encoded):
            value = encoded.pop(0)
            
            if value == NONE:
                return None

            node = TreeNode(value)
            node.left = dfs(encoded)
            node.right = dfs(encoded)
            
            return node

        return dfs(encoded)
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))