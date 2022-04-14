class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        nums.sort()
        
        max_len, curr_len = 1, 1
        
        # iterate over list starting from second index
        i = 1
        while i < len(nums):
            while i < len(nums) and nums[i] == nums[i - 1]:
                i += 1

            if i < len(nums) and nums[i] == nums[i - 1] + 1:
                curr_len += 1
                max_len = max(max_len, curr_len)
                i += 1
        
            else:
                curr_len = 1
                i += 1
                
        return max_len
            
        