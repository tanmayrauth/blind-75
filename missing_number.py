

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        return int((n*(n+1)/2) - sum(nums))




class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        # Understand why here we need res as len(nums) bcoz the range is from 0 to n included and our for loop runs untill n-1 only
        res = len(nums) 
        
        for  i in range(len(nums)):
            res ^= i ^ nums[i]

        return res