import math

class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if k == 1:
            return 0
        nums.sort()
        l = len(nums)
        diff = math.inf
        ind = k-1
        for i in range(l-ind):
            diff = min(diff, nums[i+ind] - nums[i])
    
        return diff
