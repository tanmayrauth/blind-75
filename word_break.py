"""
I would suggest first understand the recursive solution first. DP solution is very easy.

Frist try to build the Recursive Tree using the word index. 
Like for index 0 you can check that from that 0 index if the element of wordDict is present or not. 
If none of them is present then return the func. 
In case any is present that try searching for the 0+wordLength index that is that next word possiblem in the string.
Keep doing this till you reach the end of array. If you reach the end it means word combination is present in your string. At this condition will act like yoiur base condition.

Now in DP you can store these values by computing the sub problem for the each index. 
Now lets say at index 6 you can make value so save it as True. 
And at index 0 you find a value possible if we consider it the next ptr value will be 6. Now dp[6] is already True. 
So dp[0] will also become True and that is your answer.
        
"""

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        dp = [ False ] * (len(s)+1)
        dp[len(s)] = True
        
        for i in range(len(s), -1, -1):
            for word in wordDict:
                
                if (i+len(word)) <= len(s) and s[i:i+len(word)] == word:
                    dp[i] = dp[i+len(word)]
                
                # Optimization for just to stop looping incase we find the ans early
                if dp[i]:
                    break 
        return dp[0]

    
