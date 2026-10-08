class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        global_max = 0
        global_max_profit = 0
        for i in range(len(prices)-1,-1,-1):
            global_max = max(global_max,prices[i])
            global_max_profit = max(global_max_profit,global_max - prices[i])
        return global_max_profit