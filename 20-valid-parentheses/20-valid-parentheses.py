class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {
            ')': '(',
            '}': '{',
            ']': '[',
        }
        
        '''
        iterate over the str
        when encounter an opening bracket, add to stack
        when encounter a close bracket, pop off stack and see if match
        '''
        stack = deque()
        
        for char in s:
            if char not in mapping:
                stack.append(char)
            elif not stack or stack.pop() != mapping[char]:
                return False
                
        return not stack
                    
        