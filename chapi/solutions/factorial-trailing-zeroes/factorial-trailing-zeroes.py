class Solution:
    def trailingZeroes(self, n: int) -> int:
        zeros = 0
        power = 5
        while power <= n:
            zeros += int(n/power)
            power *= 5
        
        return zeros