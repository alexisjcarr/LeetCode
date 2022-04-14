cache = {}

class Solution(object):
    def climbStairs(self, n):
        if n in cache:
            return cache[n]
        
        else:
            if n <= 2:
                cache[n] = n
            else:
                cache[n] = self.climbStairs(n-2) + self.climbStairs(n-1)
                
            return cache[n]
        