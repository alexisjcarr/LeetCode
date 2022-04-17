from collections import Counter, defaultdict


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window_start, freq_hash = 0, defaultdict(int)
        s1_freq_hash = Counter(s1)
        
        for window_end in range(len(s2)):
            freq_hash[s2[window_end]] += 1
            
            if window_end - window_start + 1 == len(s1):
                if s1_freq_hash == freq_hash:
                    return True
                else:
                    freq_hash[s2[window_start]] -= 1
                    if freq_hash[s2[window_start]] == 0:
                        del freq_hash[s2[window_start]]
                    window_start += 1
                
        return False
     