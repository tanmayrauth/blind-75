"""
Reusing the logic of Rob1 question pattern. 
Here if you see we are calling the helper function on 2 set and picking out max from it. 
When we exclude the left extreme and right extreme it means that there will be no condition that it will be adj to the last or the first element.

"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def helper(houses):
            rob1, rob2 = 0, 0 
            
            for n in houses:
                temp = max(rob1 + n, rob2)
                rob1 = rob2
                rob2 = temp
                
            return rob2
                
        return max( nums[0], helper(nums[1:]), helper(nums[:-1]) )