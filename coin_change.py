import sys

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        n = len(coins) 
        dp = [[ 0 for i in range(amount+1) ] for j in range(n+1) ]
        
        for i in range(n+1):
            for j in range(amount+1):
                
                if j == 0:
                    dp[i][j] = 0
                elif i == 0:
                    dp[i][j] = sys.maxsize
                elif coins[i-1] > j:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = min( 1+dp[i][j-coins[i-1]], dp[i-1][j] )
        
        return  -1 if dp[n][amount] == sys.maxsize else dp[n][amount]