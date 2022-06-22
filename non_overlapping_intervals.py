"""
The logic is very much similar to merge interval problem (Loop + IF Else). 
Just instead of output array we keep track of elements in prevEnd variable.

Sorting is must and saving the PrevEnd value is also imp because using that only we determine whether our current bar is overlapping or not. 
Along with it we update the prevEnd with the min across currentEnd and prevEnd because we want to minimise overlapping. 
So bar with shorter length is always beneficial.  

"""

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort() 
        prevEnd = intervals[0][1]
        count = 0
        
        for start, end in intervals[1:]: 
            if start >= prevEnd:
                prevEnd = end
            else:
                count += 1
                prevEnd = min(end, prevEnd)
                
        return count