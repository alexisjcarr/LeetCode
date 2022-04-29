import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:            
        max_heap = nums
        heapq._heapify_max(max_heap)
        
        for _ in range(k - 1):
            heapq._heappop_max(max_heap)
            
        return heapq._heappop_max(max_heap)
    
