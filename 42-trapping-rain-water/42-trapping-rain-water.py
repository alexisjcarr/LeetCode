class Solution:
    def trap(self, heights: List[int]) -> int:
        if not heights:
            return 0
        
        left, right = 0, len(heights) - 1
        left_max, right_max = heights[left], heights[right]
        
        total_water = 0
        
        while left < right:
            if left_max < right_max:
                left += 1
                left_max = max(left_max, heights[left])
                total_water += left_max - heights[left]
                
            else:
                right -= 1
                right_max = max(right_max, heights[right])
                total_water += right_max - heights[right]
                
        return total_water
  
