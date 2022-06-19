class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = []
        for key in s:
            if key.isalpha() or key.isdigit():
                s1.append(key.lower())
        
        return s1 == s1[::-1] 
        