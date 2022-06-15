"""
Logic is to solve this probelm in O(n) time complexity. So, we make a pass from left to right keep a cumulative multiplication value.
Similarly we multiply from right to left. Just keep in mind the 2nd loop criteria. Since, here you won't directly assign value instead 
you will be doing this ans[i] *= ptr

"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        ans = [1] * len(nums)
        
        ptr = 1 
        for i in range(1, len(nums)):
            ptr   *= nums[i-1]
            ans[i] = ptr
            
        ptr = 1
        for i in range(len(nums)-2, -1, -1):
            ptr    *= nums[i+1]
            ans[i] *= ptr
            
        return ans
            