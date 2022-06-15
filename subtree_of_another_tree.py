"""
Thinking about base logic we can say that when we see that subroot val matches with any node value of the tree. Then we run a same tree algorithm.
So, how we can implement it is that 3 variable left, right and res

res is the result of the isSameTree check incase 2 nodes are same. 
Now then we can return the value, if any of them is True then we have a subtrees present so we always 
return left or right or res

Make sure that the base condition for None root returns False. Since we need to compare on Nodes which has values and not None.

"""


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
         
        if not root:
            return False
        
        left  = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)
        res   = False
        
        if root.val == subRoot.val:
            res = self.isMatch(root, subRoot)
              
        return  left or right or res
    

    # Algorithm is same as IsSameTree    
    def isMatch(self, root, sub_root):
        if not root and not sub_root:
            return True
        
        # If it reaches and have True condition it means one node is Null and other have Value. Which makes it a non copy tree
        if not root or not sub_root:
            return False 
        
        if root.val != sub_root.val:
            return False
        
        return self.isMatch(root.left, sub_root.left) and self.isMatch(root.right, sub_root.right)