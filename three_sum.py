"""
Understand that to find each combination we need two loops and for that we need to sort list. This problem can be solved using logic of 2sum-II. 
Now for each index we will have a while loop with 2 ptr - left and right. 
First we see if the total of 3 is less than or more than or equal to 0. Then accordingly we update l and r. 

Duplicate handling:
At the start of first loop you can check if that element is num == nums[i-1] then skip it.
When the sum is equal to 0 we need to make sure to skip all the next duplicate left elements. So for that we need an extra while loop.


"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
                 
        res = []
        nums.sort()
        
        for i, num in enumerate(nums):
            
            # Skip the duplicate same number, since we don't want repeated pattern
            if i>0 and num == nums[i-1]:
                continue
                
            l, r = i+1, len(nums)-1
            while l<r:
                total = num + nums[l] + nums[r]
                
                if total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
                else:
                    res.append([num, nums[l], nums[r]])
                    l += 1
                    
                    # Skip the duplicate same number, since we don't want repeated pattern
                    while nums[l] == nums[l-1] and l<r:
                        l += 1
                        
        return res