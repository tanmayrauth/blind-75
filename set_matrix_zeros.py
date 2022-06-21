"""
Make the 0th row and 0th column as tracker.
Understand how [0][0] edge case is handled. It is only used for 0th row tracking.
Now you have all the 0 informtion sotored in 0th row and column.
Run a double loop from 1toC and 1toR to set all inner values as 0.
At last set the 0th row and column based on the flag value of [0][0] and iscol flags.
 """

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        R = len(matrix)
        C = len(matrix[0])
        isCol = False
        
        for i in range(R):
            if matrix[i][0] == 0:
                isCol = True
                
            for j in range(1,C):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        
        for i in range(1,R):
            for j in range(1,C):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0 

        if not matrix[0][0]:
            for i in range(C):
                matrix[0][i] = 0
                 
        if isCol:
            for i in range(R):
                matrix[i][0] = 0