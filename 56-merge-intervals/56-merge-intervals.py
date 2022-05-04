class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda i: i[0])
        
        merged_intervals = [intervals[0]]
        
        for start, end in intervals:
            _, last_end = merged_intervals[-1]
            
            if start <= last_end:
                merged_intervals[-1][1] = max(end, last_end)
            
            else:
                merged_intervals.append([start, end])
                
        return merged_intervals
        