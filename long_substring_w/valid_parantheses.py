"""
Logic is that we need to take care when we see closing braces. 
It is mandatory that when we see a closing braces then the top of stack must have its corresponding opening braces else we must return false
Else we will just add the current element to stack

"""

class Solution:
    def isValid(self, s: str) -> bool:
        mapping = { ')' : '(', '}' : '{', ']' : '[' }
        stack = []
        
        for i in s: 
            if i in mapping.keys(): 
                if stack and stack[-1] == mapping[i]:
                    stack.pop() 
                else:
                    return False
            else:
                stack.append(i)
        
        return False if stack else True