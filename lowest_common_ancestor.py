"""
Intuition is you need to do DFS and search where p and q are present. Once you find them you need to return True.
Now here the catch is what you're getting from left and right. If both are true then the current node is your ans.
Also you need to make sure that your current node can be p or q as well.

DFS Logic:
    Base: If None return None -> If reached the end of a branch, return False.
    Left and Right recursion
    mid logic just to make sure if current_node == p or current_node == q
    Use left mid and right value to compare if sum is greater than equal to 2 then save that value in instance ans variable

Note:
    See how init is used inside a function.

"""


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def __init__(self): 
            self.ans = None
        
        def recurse_tree(current_node): 
            if not current_node:
                return False

            left  = recurse_tree(current_node.left) 
            right = recurse_tree(current_node.right) 
            mid   = current_node == p or current_node == q

            # If any two of the three flags left, right or mid become True.
            if mid + left + right >= 2:
                self.ans = current_node
 
            return mid or left or right
 
        recurse_tree(root)
        return self.ans