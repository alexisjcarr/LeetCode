class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_idx, max_profit = 0, 0
        
        for sell_idx in range(1, len(prices)):
            if prices[buy_idx] > prices[sell_idx]:
                buy_idx = sell_idx
            else:
                max_profit = max(max_profit, prices[sell_idx] - prices[buy_idx])
                
        return max_profit
        