from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window_start, max_length = 0, 0
        freq_hash = defaultdict(int)
        max_freq = 0
        
        for window_end in range(len(s)):
            freq_hash[s[window_end]] += 1
            max_freq = max(max_freq, freq_hash[s[window_end]])
            
            # unhappy case where move pointer
            if (window_end - window_start + 1) - max_freq > k:
                freq_hash[s[window_start]] -= 1
                window_start += 1
                
            # happy case if len(fh) == 2 and one of the values == k 
            max_length = max(max_length, window_end - window_start + 1)
            
        return max_length
            
        