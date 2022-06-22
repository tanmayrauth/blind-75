"""
Minimun no of conference room requried is simply finding the no of overlapping meeting. 
Lets say there are 2 overlapping meeting then we will definitely need 2 rooms to conduct then individually. 
So now Visualize the meeting timeline draw it you will realise that if you draw a straight line you will find the no of overalapping meeting. 
This can be acheived by maintaining 2 array start and end. 
Which will have all the start points and end points respectively. 
Next you will run the while loop Inside it you will keep on checking if start[s] < end[e]: s+= 1 count+= 1 else: e+= 1 count-=1.  
And in every loop cycle you will use max func to set value of result using current count value
"""

class Solution:
    def minMeetingRooms(self, intervals):
        start = sorted( [ i.start for i in intervals ] )
        end   = sorted( [ i.end for i in intervals ] )

        res = count = s = e = 0

        while s < len(start): # Since it is always expected that start array will exhaust before end array while traversing.

            if start[s] < end[e]:
                s += 1
                count += 1
            else:
                count -= 1
                e += 1

            res = max(res, count) 
        return res