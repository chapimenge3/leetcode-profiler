class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_total = -10**4 - 1
        cur = 0
        
        for i in nums:
            cur += i
            max_total = max(max_total, cur)
            cur = 0 if cur < 0 else cur
        
        return max_total