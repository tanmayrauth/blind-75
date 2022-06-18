"""
first element in pre-order is root, elements left of root in in-order are left subtree, right of root are right subtree, recursively build subtrees;  
Use the element to create a Tree Node and assign left and right value to it using the recursive dfs call, 
with the list splicing logic of preorder and inorder list passed to that recursive function to the respective left and right calls.
"""

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        if not preorder or not inorder:
            return None
        
        val = preorder[0] 
        idx = inorder.index(val)
         
        root = TreeNode(val)
        root.left  = self.buildTree(preorder[1:idx+1], inorder[:idx])
        root.right = self.buildTree(preorder[idx+1:], inorder[idx+1:])
        
        return root