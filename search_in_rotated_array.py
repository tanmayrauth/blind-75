"""
Solution is similar to binary search. Just here you need to understand first you're in left or right segment.
Now when you understand you are in which segment then apply logic
In left sorted portion: 
    this condition makes sure that for a mid value will always be greater for left size and less for right size. 
    Just imagine 456123 think for condition of 2&5
    In left segment you will have scenario of updating left ptr(l = mid+1) if  target > nums[mid] or target < nums[l] # This is scenario that you want to push mid and left ptr towards right
    else you update right ptr

"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        
        # THink logically it is a very self explanatory solution
        while l<=r:
            mid = l+(r-l)//2
            if nums[mid] == target:
                return mid
             
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]: 
                    l = mid + 1 
                else:
                    r = mid - 1
            
            # In right side portion
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1 
                else:
                    l = mid + 1
                    
        return -1