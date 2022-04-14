class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = [0, 1]
        
        for center in range(1, len(s)):
            odd = self.get_longest_palindrome_for(s, center - 1, center + 1)
            even = self.get_longest_palindrome_for(s, center - 1, center)
            
            local_longest = max(odd, even, key=lambda x: x[1] - x[0])
            longest = max(local_longest, longest, key=lambda x: x[1] - x[0])
        
        return s[longest[0]: longest[1]]
            
            
    def get_longest_palindrome_for(self, s, left, right):
        while left >= 0 and right < len(s):
            if s[left] != s[right]:
                break
            left -= 1
            right += 1
        return [left + 1, right]
        