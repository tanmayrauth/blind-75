"""
intervals = [(0,30), (5,10), (15,20)]
output = False

Since there is conflict in intervals of meetings. So, a person can't attend all the meeting. 
We need to find it person can attend all of it ?

The solution is similar to finding out if the interval is overlapping to other or not. 
So first thing you know for such problem is to sort it.
Then starting from index 1 every time we check that is our current start overlapping with the previous end.
If overlapping : return False
Else at end of loop return True

"""

class Solution:
    def canAttendMeetings(self, intervals):

        intervals.sort( key = lambda i: i.start )

        for i in range(1, len(intervals)):
            i1 = intervals[i-1]
            i2 = intervals[i]

            if i1.end > i2.start:
                return False

        return True