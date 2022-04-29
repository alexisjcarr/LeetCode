class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()

        i = 0
        for num in nums:
            if num == i:
                i += 1

        return i
        