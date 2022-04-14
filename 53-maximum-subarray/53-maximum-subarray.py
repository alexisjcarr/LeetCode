class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_max, global_max = nums[0], nums[0]
        
        for idx in range(1, len(nums)):
            if current_max < 0:
                current_max = nums[idx]
            else:
                current_max += nums[idx]
            global_max = max(current_max, global_max)
        return global_max
        