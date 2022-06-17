"""
Intuition is whenever you have something to find contiguious. You can use Sliding window, since here you need to keep unique elemets. 
So, we can need to track of the current elem present in window using a set. Simple sliding window + set logic. 

For Loop which will act like right ptr.
Inside it a while loop will check that if the right ptr is already present in set.
    If Yes then keep popping elements from left till the old right ptr element is not removed from set 
    left ptr will be incremented each time. 
Once this is done add this new right ptr elem to set
Measure the string length using max function.

"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = ans = 0
        tracker = set()
        
        for right in range(len(s)): 
            while s[right] in tracker:
                tracker.remove(s[left])
                left += 1
            tracker.add(s[right])
            ans = max( ans, right - left + 1)
            
        return ans