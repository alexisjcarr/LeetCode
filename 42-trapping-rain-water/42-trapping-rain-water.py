class Solution:
    def trap(self, heights: List[int]) -> int:
        total_water = 0
        
        # build up the left array
        left = self.find_max_array(heights)
        
        # build up the right array
        right = self.find_max_array(heights[::-1])[::-1]
        
        # iterate through the heights array (indices)
        for i in range(len(heights)):
            total_water += min(left[i], right[i]) - heights[i]
        
        return total_water
    
    
    def find_max_array(self, heights: List[int]) -> List[int]:
        res = []
        
        max_ = 0
        
        for height in heights:
            max_ = max(max_, height)
            res.append(max_)
            
        return res
        
        