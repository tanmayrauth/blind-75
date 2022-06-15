"""
DFS + Mapping for visited Node + BIH logic

DFS Logic:
    If node is present in mapping
    If node is not present in mapping
    Run a loop over neighbors to set value for newNode neighbors
    return the newNode since you have fully created it along with its neighbors

"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        if not node:
            return None
        
        nodeMapping = {}
        def dfs(node):
            if node in nodeMapping:
                return nodeMapping[node]
            
            newNode = Node(node.val)
            nodeMapping[node] = newNode
            
            for n in node.neighbors:
                newNode.neighbors.append( dfs(n) )
            return newNode
        
        return dfs(node)
