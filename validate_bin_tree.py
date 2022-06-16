"""
I would suggest comparing the logic of this question with isSameTree question.
Recursive in order traversal: 
    Base Condition: If None: return True -> If we're reaching till the end then we have valid tree till that pt.
    We need to check if the curr Node value fits properly in the bounds(min and max): 
        min value < node.val < max value    -> If this doesn't hold true return False
        recurse left -> bound max to node.val since anything on left should be less.   
        recurse right -> bound min to node.val since anything on right should be greater
        return left and right
"""

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool: 
        
        def helper(node, minv=float('-inf'), maxv=float('inf')):
            if not node:
                return True
            
            # minv < val < maxv
            if not (node.val > minv and node.val < maxv ):
                return False
            
            # branch and bound left child -> bound max
            b1 = helper(node.left, minv, node.val)
            
            # branch and bound right child -> bound min
            b2 = helper(node.right, node.val, maxv)
            
            return b1 and b2 
            
        return helper(root)
