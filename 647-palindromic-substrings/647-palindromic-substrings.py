class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        
        for i in range(len(s)):
            # count center
            count += 1
            
            # count odd pals
            count += self.countPals(s, i - 1, i + 1)
            
            # count even pals
            count += self.countPals(s, i - 1, i)
        return count
    
    
    def countPals(self, s: str, left: int, right: int) -> int:
        count = 0
        
        while left >= 0 and right < len(s):
            if s[left] != s[right]:
                break
            
            left -= 1
            right += 1
            
            count += 1
            
        return count
        