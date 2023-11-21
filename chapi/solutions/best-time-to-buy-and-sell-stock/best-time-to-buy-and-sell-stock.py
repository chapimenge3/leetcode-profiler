class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        _min = prices[0]
        profit = 0
        for i in prices[1:]:
            _min = min(i, _min)
            profit = max(profit, i - _min)
        
        return profit
