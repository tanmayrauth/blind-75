"""
Here first we need to understand for a particular index amongst all 32 index what value does it hold (1 or 0).
For that we can do  & or % modulo operation on n. But here you need to make sure to shift the bits to rightmost end then only you will get to know the value of that bit. 
Now you got the bit value. Next thing we need to do is to move this value to the left most extremene. Since we want to reverse the string. The best way to do this is to use 'or' operation. 1 or 0 = 1, 1 or 1 = 1.
That way your current values sotred in res won't get impacted.

"""

class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        
        for i in range(32):
            bit = (n >> i) & 1
            res = res | bit << (31-i)
            
        return res