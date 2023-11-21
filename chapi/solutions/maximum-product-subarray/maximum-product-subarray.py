class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mx, mn = 1, 1
        res = max(nums)
        for i in nums:
            if i == 0:
                mx, mn = 1, 1
            else:
                tmp = mx * i
                mx = max(i * mx, i * mn, i)
                mn = min(tmp, i * mn, i)
                res = max(res, mx)
            
        return res


