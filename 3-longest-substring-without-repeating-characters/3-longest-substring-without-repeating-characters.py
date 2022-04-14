class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window_start, max_length = 0, 0 
        
        visited = set()
        
        for window_end in range(len(s)):
            while s[window_end] in visited:
                visited.remove(s[window_start])
                window_start += 1
                
            visited.add(s[window_end])
            max_length = max(max_length, window_end - window_start + 1)
            
        return max_length
            