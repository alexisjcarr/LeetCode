from collections import Counter
import heapq


class Solution:
    def frequencySort(self, s: str) -> str:  # O(nlogn) time | O(n) space
        res = ""
        freq_hash = Counter(s)
        
        max_heap = [(count, letter) for letter, count in freq_hash.items()]
        heapq._heapify_max(max_heap)
        
        while max_heap:
            count, letter = heapq._heappop_max(max_heap)
            res += letter * count
                
        return res
      
