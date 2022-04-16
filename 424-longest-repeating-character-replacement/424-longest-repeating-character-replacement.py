from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        "ABAB", k = 2
        
        {
            A: 2,
            B: 2
        }
        
        s = "AABABBA", k = 1
        
        approach: i think we can do a sliding window with a freq_counter (will optimize later)
            if one of the elements in the counter is equal to k AND the counter only has two items
            then we can include that substring
        '''
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
            
        