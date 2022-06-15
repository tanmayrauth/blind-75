"""
This is graph problem since you're creating a directed graph using the data and using it you need to check if cycle is present.
DFS traversal of a graph:  Loop over all nodes + tracking/visited set 

DFS:
    Base Condn:
        Does it have Adj Nodes
        Is the node present in track/visited set

    Backtracking logic for visited set before and after the loop
    Loop over it adj Nodes and call DFS for it and each time you will check if you have received False from them or not.
    At last return True if all is Good. Since till this point you have checked all the adj node of current node and they didn't gave you cycle for current node and its parent.
 
"""

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adjList = { i:list() for i in range(numCourses) }
        
        for crs, pre in prerequisites:
            adjList[crs].append( pre )
          
        trackSet = set() 
        def dfs(node):
            if not adjList[node]:
                return True
            if node in trackSet:
                return False
            
            trackSet.add(node)
            for n in adjList[node]:
                if not dfs(n): return False
            trackSet.remove(node)
            
            adjList[node] = [] # Optimization purpose, since we know that this node has been tracked
            return True
        
        for node in range(numCourses):
            if not dfs(node): return False
            
        return True
