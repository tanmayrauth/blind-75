"""
Understand recursion here
Base:
    If None then return 0
Induction + Hypothesis:
    You need left and right values. Take make of it and add 1 to it.

"""

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        left = self.maxDepth(root.left) 
        right = self.maxDepth(root.right)
        
        return max(left, right) + 1