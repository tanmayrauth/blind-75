class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        r = len(matrix)
        c = len(matrix[0])  if r else 0
        
        if not c:
            return []
        
        top = left = 0
        right = c-1
        bottom = r-1
        result = []
        
        while True:
            
            for i in range(left, right+1):
                result.append(matrix[top][i])
                
            top += 1 
            if top>bottom:
                break
                
            for i in range(top, bottom+1):
                result.append(matrix[i][right])
                
            right -= 1    
            if left>right:
                break
            
            for i in range(right, left-1, -1 ):
                result.append(matrix[bottom][i])
                
            bottom -= 1
            if top > bottom:
                break
                
            for i in range(bottom, top-1, -1):
                result.append(matrix[i][left])
            
            left +=1
            if left>right:
                break
                
        return result
            
            