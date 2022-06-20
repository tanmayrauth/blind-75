
"""
Logic is to understand for reaching path m,n from m-1,n you have only 1 way, 
Similary from m, n-1 location you have only 1 path. 
Now any cell in middle of the matrix will have path sum eqaul to dp[i][j+1] + dp[i+1][j]. Because from this location you are allowed to move only right or down.
So now you understand the whole last row and col will have only 1 path to reach till m,n cell.

"""

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:   
        
        dp = [[1 for j in range(n)] for i in range(m)]
        
        for j in range(n-2,-1,-1):
            for i in range(m-2,-1,-1):
                dp[i][j] = dp[i][j+1] + dp[i+1][j]
                
        return dp[0][0]
        