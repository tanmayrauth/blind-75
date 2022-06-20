"""
Simple approach is to track the max jump I can take. 
Update the max jump variable only if it is less than the current nums index value. 

Keep on checking that if that maxValue is the value 0 along with index < array length.
    If yes then return False.

At the end of each cycle reduce value of max jump var. 
"""

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxJump = 0
        
        for i, j in enumerate(nums):
            maxJump = max(maxJump, j)
             
            if maxJump == 0 and i < len(nums)-1:
                return False
            
            maxJump -= 1
            
        return True