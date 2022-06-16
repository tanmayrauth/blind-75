"""
Logic is that you will run through indices and keep on summing up values. 
Now for each index you have to choose whether to pick the summed up value or current index value. 
You will choose summed up value with prev only if it is greater than current index value. This is done using max function.
"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sumArray = list()
        
        sumArray.append(nums[0])
        for i in range( 1, len( nums ) ):
            sumArray.append( max( nums[i] + sumArray[i-1], nums[i] ) )
            
        return max( sumArray )