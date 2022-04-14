class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # each the value at each index in lengths represents the length of the longest subsequence until until the corresponding index in nums
        lengths = [1 for _ in nums] 
        
        for i, last_num in enumerate(nums):
            for j in range(i):
                prior_num = nums[j]
                
                if prior_num < last_num and lengths[i] <= lengths[j] + 1:
                    lengths[i] = lengths[j] + 1
                    
        return max(lengths)
        
        
        