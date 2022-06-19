"""
Initialise the res with first index. 
The logic is to first check in which portion you're currently in. 
Left or right now based upon that you will increment or decrement your left or right ptr respectively using binary search format. 
Your goal will be to push your mid index towards the right. 
Once you have reached it then using min function you will update the res with value of nums[m]
        
"""

class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        res = nums[0]
        l, r = 0 , len(nums)-1
        
        while l <= r:
            if nums[l] < nums[r]: # Edge condtion of no rotate will be handeled as well
                res = min(res, nums[l])
                break
                
            mid = (l+r) // 2
            res = min(res, nums[mid])
            if nums[mid] >= nums[l]:
                l = mid +1
            else:
                r = mid -1
                
        return res