"""
Noob approach will be to find out all the substrings using the recursion and then check if that substring is a pallindrom or not. 
Or This can be solved by a naive approach by forming all the substring using 2 for loops i:1-> n and i->n then checking if that substring is a pallindrome.
o(n) will be pallindrome check and o(n2) will be complexity for finding substrings

So best stragegy is to find the pallindrom for each index. By moving ptr to left and right till the extrement and checking if it is pallindrome or not. 
Just imp factor is that you need run it once for Even and once for odd.

Question is relatd to 647. Palindromic Substrings
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
         
        res = ""
        resLen = 0
        
        for i in range(len(s)):
            l, r = i, i
            
            while l>=0 and r < len(s) and s[l] == s[r]:
                if r-l+1 > resLen:
                    resLen = r-l+1
                    res = s[l:r+1]
                r += 1
                l -= 1
                
        for i in range(len(s)):
            l, r = i, i+1
            
            while l>=0 and r < len(s) and s[l] == s[r]:
                if r-l+1 > resLen:
                    resLen = r-l+1
                    res = s[l:r+1]
                r += 1
                l -= 1
                
        return res