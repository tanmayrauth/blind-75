"""
We can't apply the same logic of maximum sum subarray. 
Since, here can be possiblity tht value can be -ve and 2 -ve values multiplied can become +ve value. 
So logic here can be that for each index we will keep on currentMin and CurrentMax then use it to find the next currentMin and currentMax. 
At the same time I will keep on checking that the currentMax is greater than result or not.

Note:
While checking max and mix compare it with current number as well
Incase a number is 0 then we need to set curMin and curMax to 1

"""

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curMin, curMax = 1, 1
         
        for i in range(len(nums)):
            
            if nums[i] == 0:
                curMin, curMax = 1, 1
                continue
            
            temp = curMin * nums[i]
            curMin = min( temp, curMax*nums[i], nums[i])
            curMax = max( temp, curMax*nums[i], nums[i])
            
            res = max(res, curMax)
            
        return res