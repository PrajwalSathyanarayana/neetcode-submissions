class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for r in range(len(matrix)): # iterate through rows in the matrix
            for c in range(len(matrix[0])): # iterate through columns in the matrix
                if target == matrix[r][c]: return True # if the target value == current value of matrix[r][c], return True
        return False # else return False

# Brute Force approach
# TC O(m*n), m and n - no. of rows and columns in the matrix
# SC O(1)