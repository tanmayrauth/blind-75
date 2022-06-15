"""
Clear intuition that we need BFS here since it is a level order traversal
While queue is not empty run for loop for the length of queue, keep poping elements from queue in each step. 
Now in each step if you see left or right element is present keep them adding to queue

For BFS you need 2 loops: 
    While loop over queue and inside for loop for poping elements from queue
"""

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root: return []
        result, queue = [], deque([root])
        
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
                    
            result.append(level)
        
        return result

