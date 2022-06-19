"""
The logic is pretty much similar to longest substring without replacement. Problem 3.

It is sliding window problem since you need to find a continuious window size for which you can replace the k elements in it and get the max elements of same values in it.
So you'll have to imply simple logic of sliding window that every time you will  have to check that the windowSize - samecharSizeInIt <= k, if it is not then incrment left ptr and reduce its count from mapping. 
And everytime in the end of loop find max amongst current win size and result 


"""

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        valueCount = dict()
        res = l = 0
        
        for r in range(len(s)):
            valueCount[s[r]] = 1 + valueCount.get(s[r], 0)
            
            while (r-l+1 - max(valueCount.values())) > k:
                valueCount[s[l]] -= 1
                l += 1
                
            res = max(res, r-l+1)
        
        return res