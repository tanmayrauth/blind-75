"""
This can be solved by a naive approach by forming all the substring using 2 for loops i:1-> n and i->n then checking if that substring is a pallindrome. But we can optmise it using some amazing approach for even and odd length. 
For even len we will start at idx and then decrement left and incrment right and check if both are same if same then increase result.
For odd len similar pattern but the init of idx will be different l=i and r=i+1
QUesiton is related to 5. Longest Palindromic Substring

Understand here why we don't need any if condition inside loop        
"""

class Solution:
    def countSubstrings(self, s: str) -> int:
        
        res = 0 
        for i in range(len(s)):
            
            # Odd length
            l = r = i
            while l>=0 and r<len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
             
            # Even length
            l, r = i, i+1
            while l>=0 and r<len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
                
        return res