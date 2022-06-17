"""
Logic is that if we sort the ranges with the starting pt this way we will get the overlapping sequences. 

Now starting from index 1 if we will always compare previous output end and current start. 
The logic says if the current start is less than previous end the the range is overlapping. 
So merge them using the max end length amongst both and assign end value with the max of previous end and current end.
        
"""

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort( key = lambda i : i[0] )
        output = [ intervals[0] ]
        
        for start, end in intervals[1:]:
            lastEnd = output[-1][1]
            
            if start <= lastEnd:
                output[-1][1] = max( lastEnd, end )
            else:
                output.append( [start, end] )
                
        return output
        