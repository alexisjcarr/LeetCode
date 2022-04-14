from collections import Counter
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res: List[int] = []
        
        # create nums freq hash
        nums_freq: Dict[int, int] = Counter(nums)
        
        # max heapify nums freq hash
        max_heap: List[Tuple[int, int]] = [(count, num) for num, count in nums_freq.items()]
        heapq._heapify_max(max_heap)
        
        # pop off the top k
        for _ in range(k):
            _, num = heapq._heappop_max(max_heap)
            res.append(num)
            
        return res
      