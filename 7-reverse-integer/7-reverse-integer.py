class Solution:
    def reverse(self, num: int) -> int:
        MIN = -2147483648
        MAX = 2147483647
        
        res = 0
        
        while num:
            digit = int(math.fmod(num, 10))
            num = int(num/10)
            
            if res > MAX // 10 or res == MAX // 10 and digit >= MAX % 10:
                return 0
            
            elif res < MIN // 10 or res == MIN // 10 and digit <= MIN % 10:
                return 0
            
            res = res * 10 + digit
            
        return res