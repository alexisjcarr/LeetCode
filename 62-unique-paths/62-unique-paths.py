from collections import deque


class Solution:
    def uniquePaths(self, m: int, n: int, memo={}) -> int:
        key = f'{m}, {n}'
        
        if key in memo: return memo[key]
        if m == 0 or n == 0: return 0
        if m == 1 and n == 1: return 1
        
        memo[key] = self.uniquePaths(m-1, n, memo) + self.uniquePaths(m, n-1, memo)
        return memo[key]


class AltSolution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 0 and n == 0:
            return 1
        
        count = 0
        stack = deque()
        stack.append([0, 0])
        
        while stack:
            r, c = stack.pop()
            
            if r == m - 1 and c == n - 1:
                count += 1
            
            # r + 1 in bounds, add to stack
            if r + 1 < m:
                stack.append([r + 1, c])
            
            # if c + 1 in bounds, add to stack
            if c + 1 < n:
                stack.append([r, c + 1])
            
        return count
        
