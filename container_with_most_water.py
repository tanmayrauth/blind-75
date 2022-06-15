"""
Intuition here is that we need to find out the max area. So for finding max area we need first max width possiblity. 
We start with left and right extreme. Now everytime we will calculate the area by picking the min height amongst both ptr. 
Now for next cycle the logic is that you will remove the one which had less height. So, based upon that you will increment or decrement the lft or right ptr.  

"""

class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        left, right = 0, len(height)-1 
        max_area    = 0
        
        while left < right:
            if height[left] < height[right]:
                area = height[left] * (right-left)
                left += 1
            else:
                area = height[right] * (right-left)
                right -= 1
                
            max_area = max(area, max_area)  
        return max_area