"""
Looking at problem you will get intuition that the logic is very similar for finding the components in graph using dfs and visited array. 
Here also we track the island using the value conversion method. So if the value is  1 then only we change value to 2 and do dfs in all 4 direction else we just return the value. 
At outer side we run 2 loop checking each cell's value everytime we see 1 then we call dfs and increment island_count. 

DFS logic:
    Base: Put all 5 False conditions for which you want to stop DFS
    change value to 2 or put that index into visited set
    Do DFS in all 4 direction

"""


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        R, C = len(grid), len(grid[0])
        total_island = 0
        
        def dfs(r, c):
            if r<0 or c<0 or c==C or r == R or grid[r][c] != '1':
                return
            grid[r][c] = '2'
            
            dfs(r-1, c)
            dfs(r+1, c)
            dfs(r, c-1)
            dfs(r, c+1)
        
        for r in range(R):
            for c in range(C):
                if grid[r][c] == '1':
                    total_island += 1
                    dfs(r, c)
                    
        return total_island