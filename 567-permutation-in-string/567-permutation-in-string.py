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
    

class AltSolution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        
        s1Count, s2Count = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1
        
        matches = 0
        for i in range(26):
            matches += (1 if s1Count[i] == s2Count[i] else 0)
        
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26: return True
            
            index = ord(s2[r]) - ord('a')
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1
            
            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
            l += 1
        return matches == 26
     
