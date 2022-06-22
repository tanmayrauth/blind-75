"""
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
             
        for vertice in range(n):            
            if vertice not in visited:
                self.dfs(vertice, adjacency_list, visited)
                count += 1
        
        return count
    
    
    def dfs(self, vertice, adjacency_list, visited):        
        visited.add(vertice)
        
        for adj_vertice in adjacency_list[vertice]:
            if adj_vertice not in visited:
                self.dfs(adj_vertice, adjacency_list, visited)   
                