# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        '''
        choose root as mdpt
        l + r
        '''
        def helper(left, right):
            if left > right:
                return None
            
            mdpt = (left + right)//2
            
            root = TreeNode(nums[mdpt])
            root.left = helper(left, mdpt - 1)
            root.right = helper(mdpt + 1, right)
            
            return root
        
        return helper(0, len(nums) - 1)
            
            
        