"""
LIS as states we need array in the same sequence of increasing order. Try creating the recursive solution using the brute force like taking the one element then add the next element and so on.
So if we run in reverse way of the list as 2nd loop and keep on adding 1 incase the condition of continuity stisfies then we should be able to do this in DP format.

To understand why we need if condition with second for loop. Imagine a case with
4, 5, 10, 6, 7, 8 -> here you can see at index 1  the value will be 2 but at index 3 the value will be 3.
So for index 0 the value should be 3+1 to get the max increasing sub seq.
         
"""


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        LIS = [1] * (len(nums))
        
        for i in range(len(nums)-1, -1, -1):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max( LIS[i], 1+LIS[j])
                    
        return max(LIS)