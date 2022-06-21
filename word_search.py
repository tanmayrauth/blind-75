""" You can do it on your own........ 
Since here it is a matrix and we are sure that we need to go through each cell and take it as start point.
So DFS is definitely there. Hence we will need a double loop and call dfs inside it.

Inside DFS: 
    We will go each index by index of word and try to match it with current cell. 
    If the current cell matches then we will try to move it in 4 directions. 
    If from any one of direction we get True we keep on moving till the end of string length.  
    Do back tracking store the 4 direction result and return it. Don't forget to maintain the visit set.
"""
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        R = len(board)
        C = len(board[0])
        visit = set()
        wordCtr = 0
        
        def dfs(r, c, wordCtr):
            if wordCtr == len(word):
                return True
            
            if r<0 or c<0 or r==R or c==C or (r,c) in visit or word[wordCtr] != board[r][c]:
                return
            
            visit.add((r,c))
            res = dfs(r+1, c, wordCtr+1) or \
                  dfs(r-1, c, wordCtr+1) or \
                  dfs(r, c+1, wordCtr+1) or \
                  dfs(r, c-1, wordCtr+1) or \
            visit.remove((r,c))
            
            return res
            
        
        
        for r in range(R):
            for c in range(C):
                if dfs(r, c, wordCtr):
                    return True
                
        return False