"""
Inutition is to think at at node level what you want to is just swap left and right
Then you want to do this same process for your left and right node. So, call a recursive func for it.
And for base condition use the the not Node condition.

"""

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # BHI logic - In induction the only thing we need to do is swap the values
        
        if not root:
            return 
        
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        root.left, root.right = root.right, root.left 
        return root