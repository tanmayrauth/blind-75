"""
Brute force way is to take each value let's say 0,1,2 and for each value do %2 and /2 till it reaches 0.
This will give the no of 1 for each value. So you can imagine it as a while loop inside a for loop. And inside while loop will run for each number and will do %2 and /2 till it reaches 0.

Our optimised approach here is that if you will a bit representation of each number. You will find a repeating pattern lets say for 4 the value is (no of 1s in 0 + 1)
Thts how we figured out that it is a DP problem and the formula will be 1 + dp[i-offset]. Offset here is the number which forms the same pattern with current one. For 4 it is 0.

"""

class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n+1)
        offset = 1
        
        for i in range(1, n+1):
            if offset * 2 == i:
                offset = i
                
            dp[i] = 1 + dp[i-offset]
            
        return dp