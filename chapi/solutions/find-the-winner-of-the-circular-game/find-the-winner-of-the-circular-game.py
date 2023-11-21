class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        return (self.findTheWinner(n-1, k) + k - 1) % n + 1 if n > 1 else 1
