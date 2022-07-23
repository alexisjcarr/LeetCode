class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hash = defaultdict(lambda: 0)
        
        for num in nums:
            hash[num] += 1
            
        for num in nums:
            if hash[num] == 1:
                return num
