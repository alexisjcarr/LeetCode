class Solution(object):
    def maxProduct(self, nums):
        """
        Modified Kadane's algorithm:
        max_so_far = A[0]
        min_so_far = A[0]
        result = max_so_far
        
        for i = 1 -> size of A
            curr
        """
        max_so_far = nums[0]
        min_so_far = nums[0]
        result = max_so_far

        for i in range(1, len(nums)):
            curr = nums[i]
            temp_max = max(curr, max_so_far * curr, min_so_far * curr)
            min_so_far = min(curr, max_so_far * curr, min_so_far * curr)

            max_so_far = temp_max

            result = max(max_so_far, result)

        return result