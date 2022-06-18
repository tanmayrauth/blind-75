"""
Logic is to find max between [1,2,3] -> 1+3 element and 2 element 
Loop this logic along the whole nums array

Understand the subproblem logic here let's say there are 4 elements. First Imagine the max amongst first 2 elements.
Now imagine the value for 4th index: it can jst be possible that you only rob 1 and 4. 
Such case is only possible by subprobelm of 1and2 in that we will choose value 1 and move forward to compute with 3rd index.

""" 

class Solution:
    def rob(self, nums: List[int]) -> int: 
        
        rob1 = rob2 = 0
        for n in nums:
            temp = max(rob1+n, rob2)
            rob1 = rob2
            rob2 = temp
            
        return rob2