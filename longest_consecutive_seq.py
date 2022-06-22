"""
Define a numset to store all the elements in the seq
Loop in add if condition to see if i-1 not in numSet: add length variable and a while loop to to keep incrementing length. 
Using this you can calculate the max consecutive sequence
"""


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        
        for i in nums:
            if i-1 not in numSet:
                length = 0
                
                while (i+length) in numSet:
                    length += 1
                longest = max(longest, length)
                
        return longest