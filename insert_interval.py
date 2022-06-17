"""
At start the question my look scary bt if you think carefully it can be solved using only 1 loop.
While runnning the loop you need to take care of conditions.
It is all about managing conditions between new and current element's start-end

Conditions:
    If: New start > Current End. # If interval[i] completely smaller than new  
    If: Current start > new End.  # If interval[i] completely greater than new
    Else: Use min and max for merging elements

The last steps:
    Apeending last new interval
    If new part extend till end than simply return merged ones
    If not till end than return merged + remainling intervals
"""

class Solution:
    def insert(self, intervals, new):
        
        merged,t,l = [], 0, len(intervals)       
        for curr in intervals:
             
            if new[0]>curr[1]:
                merged.append(curr) 
            elif curr[0]>new[1]:
                break 
            else:               
                new[0] = min(new[0], curr[0])
                new[1] = max(new[1], curr[1]) 
            t+=1 
            
        merged.append(new) 
        return merged+intervals[t:] if t<l else merged

