class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        m = prices[0]
        profit = 0
        for i in range(1, len(prices)): 
            profit = max( prices[i] - m, profit )
            m = min( m, prices[i] )
             
        return profit
        