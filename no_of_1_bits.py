"""
When we do a % 2 it is all about the right most bit's value.
So if we keep on checking %2 and everytime we shift the bit to right then we can get our ans. 
Since our %2 operation will be operated on right most bit. 
And we will keep on running this till all the values becomes 0 and our while loop breaks.
"""

class Solution:
    def hammingWeight(self, n: int) -> int:
        
        res = 0
        while n:
            res += n%2
            n = n >> 1
            
        return res