"""
Using preorder traversal + DFS you can create a string first and then use that string to create a live tree again
Try to think why inorder traversal is not used here.
If we use inorder then during deserialze the first element will be None and that will be return by the first if condition

During deserialise we don't need to keep track of the count < len(vals) because during serialization we had already covered both left and right.
"""

class Codec:

    def serialize(self, root):
        res = []
        
        def dfs(node):
            if not node:
                res.append('N')
                return 
            
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
            
        dfs(root)
        return ','.join(res)
        

    def deserialize(self, data):
        vals = data.split(',')
        self.count = 0
        
        def dfs():
            if vals[self.count] == 'N':
                self.count += 1
                return None
            
            node = TreeNode(int(vals[self.count]))
            self.count += 1
            node.left = dfs()
            node.right = dfs()
            
            return node
        
        return dfs()