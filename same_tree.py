"""
This about your return value first then you will realise that here your left and right should return True only then your tree is same. 
Now the recursive func will have 3 base condition: 
    p and q both are none
    p or q is none
    p and q does not has same value

Understand here we haven't used anywhere the condition to check both are same. It is automatically handled in base case and return value.    
"""


class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """    
        # p and q are both None
        if not p and not q:
            return True
        # one of p and q is None
        if not q or not p:
            return False
        if p.val != q.val:
            return False
        
        return self.isSameTree(p.right, q.right) and \
               self.isSameTree(p.left, q.left)