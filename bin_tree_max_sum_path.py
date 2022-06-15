"""
So here we need is Recursion + res value

Recursion Logic:
    Base: return 0 when None
    Run for left and right recursion
    Compare child sum values with current node value
    Checking a scenario of the current node becomes common node
    Checking max with global res values and current ans
    return the child node sum values since it will be used later by parent nodes

"""

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = root.val  # We can't initialise 0 here, since node values can be negative
        self.solve( root ) 
        return self.res
        
        
    def solve(self, root):
        if not root: # Base Condition
            return 0
        
        l = self.solve(root.left)
        r = self.solve(root.right)
        
        temp = max( max(l, r) + root.val, root.val ) # Comparing child sum values with current node value
        ans  = max(temp, l + r + root.val )   # Checking a scenario of the current node becomes common node
        self.res = max( self.res, ans )    # Checking max with global values
         
        return temp  # return the child node sum values since it will be used by parent nodes
