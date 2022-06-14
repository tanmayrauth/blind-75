"""
Create a mapping dict for array values and their corresponding index, incase while searching for diff in mapping is not present. Run this logic over each elements using for loop.

"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping = {}
        
        for index, value in enumerate(nums): 
            diff = target - value
            if diff in mapping:
                return [mapping[diff], index]
            else:
                mapping[value] = index