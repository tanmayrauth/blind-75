"""
Noob approach is create all combinations using 2 loops
Here we want to do it in single loop for that reason we need a mapping of array value to index. 
So while searching for diff(Target - array val) in mapping if it is not present then we add its index to mapping. 
So in next iteration if some element has diff equal to this index value then we can return the result.
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