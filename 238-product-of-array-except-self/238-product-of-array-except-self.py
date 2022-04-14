class Solution(object):
    def productExceptSelf(self, nums):  # [1,2,3,4]
        left, right = 1, 1
        product = []  # [1, 1, 2, 6, 24]
        
        for num in nums:
            product.append(left)
            left *= num
            
        for idx in range(len(nums) - 1, -1, -1):
            product[idx] *= right
            right *= nums[idx]
            
        return product
        