class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        
        visited = set()
        
        i = 1
        for num in nums:
            if num <= 0 or num in visited:
                continue
                
            elif num != i:
                return i
            
            i += 1
            visited.add(num)
                
        return i
        