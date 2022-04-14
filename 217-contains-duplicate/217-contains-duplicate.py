class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count = defaultdict(lambda: 0)
        
        for num in nums:
            count[num] += 1
            
            if count[num] == 2:
                return True
            
        return False
        