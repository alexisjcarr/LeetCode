class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        count = defaultdict(lambda: 0)
        
        for num in nums:
            count[num] += 1
            
            if count[num] == 2:
                return num
        