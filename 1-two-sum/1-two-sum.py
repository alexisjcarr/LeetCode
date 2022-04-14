class Solution(object):
    def twoSum(self, nums, target):
        hash = {}
        
        for idx, num in enumerate(nums):
            desired = target - num
            if desired in hash:
                return [idx, hash[desired]]
            hash[num] = idx
        