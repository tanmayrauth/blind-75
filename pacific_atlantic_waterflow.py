"""
Naive logic is to do DFS in each cell to find if it reaches extreme but that will have M*N^2 TC. 
Better approach will be that we go from edges to the middle. Logic is that we will go for edges of all 4 sides to internal cells. 
We will maintain 2 set pacific and atlantic using which we will keep on adding element for which the height is greater than previous height: which start from as edge cell height.

So if the edge cell height is lower than inner cell then only the water will flow till edge. This way we will have 2 sets. Among these 2 sets the common cells are the ones for which water will reach to both atlantic and pacific.

DFS:
    Base Condition: Matrix boundary condition and prevHeight > current height then return None
    Add Element to the pacific/atlantic visited set
    Run DFS in 4 direction
            
"""

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
   
        R, C = len(heights), len(heights[0])
        pac, atl = set(), set()
        
        def dfs(r, c, visit, prevHeight):
            if r<0 or c<0 or r == R or c == C or (r, c) in visit or heights[r][c] < prevHeight :
                return
            visit.add((r, c))
            dfs(r, c+1, visit, heights[r][c])
            dfs(r, c-1, visit, heights[r][c])
            dfs(r+1, c, visit, heights[r][c])
            dfs(r-1, c, visit, heights[r][c])
            
        for c in range(C):
            dfs(0, c, pac, heights[0][c])
            dfs(R-1, c, atl, heights[R-1][c])
            
        for r in range(R):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, C-1, atl, heights[r][C-1])
             
        result = list()    
        for i in range(R):
            for j in range(C):
                if (i, j) in pac and (i, j) in atl:
                    result.append((i, j))

        return result
