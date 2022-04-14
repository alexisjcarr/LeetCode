from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        
        for s in strs:
            sorted_word = ''.join(sorted(s))
            
            res[sorted_word].append(s)
            
        return list(res.values())
      