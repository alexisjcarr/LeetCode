from collections import Counter
import heapq


class Solution:
    def frequencySort(self, s: str) -> str:
        '''
        {
            t: 1,
            r: 1,
            e: 2
        }
        
        max_heap = [(count, letter) for letter, count in hash]
        
        pop off heap and add to str
        '''
        res = ""
        freq_hash = Counter(s)
        
        max_heap = [(count, letter) for letter, count in freq_hash.items()]
        heapq._heapify_max(max_heap)
        
        while max_heap:
            # pop off heap
            count, letter = heapq._heappop_max(max_heap)
            
            for _ in range(count):
                res += letter
                
        return res
        
        
        