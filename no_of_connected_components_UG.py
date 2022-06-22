"""
It is actualy a king of no of island problem. 
Jst here it will be one loop whereas in matrix ther will be 2 loop required.
This problem is solved using DFS. We can also solve this using Union Find algorithm.

Kind of similar to LC 547
"""

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        count = 0 
        visited = set() 
        adjacency_list = []
        
        for i in range(n):
            adjacency_list.append([])
            
        for edge in edges:
            adjacency_list[edge[0]].append(edge[1])
            adjacency_list[edge[1]].append(edge[0])
             
        for node in range(n):            
            if node not in visited:
                self.dfs(node, adjacency_list, visited)
                count += 1
        
        return count
    
    
    def dfs(self, node, adjacency_list, visited):        
        visited.add(node)
        
        for adj_node in adjacency_list[node]:
            if adj_node not in visited:
                self.dfs(adj_node, adjacency_list, visited)   
                