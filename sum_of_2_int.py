"""
Only in Python we need this masking logic. Else its just simple logic.
That we will do a xor on 2 numbers first. Then for identifying carry we will use & operation and shift it to left by 1 bit. Then this new & number and result of xor will be then used in next cycle.

"""

class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        
        while b:
            carry = (a & b)<<1
            a = (a ^ b) & mask
            b = carry & mask
        
        return ~(a^mask) if mask//2 < a else a