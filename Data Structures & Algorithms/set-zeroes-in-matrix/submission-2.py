class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0]) # no of rows, cols
        rowZero = False # Tracks whether the first row needs to be zeroed; matrix[0][0] is shared by the first row and first column, so we need a separate variable to track the first row independently.

        # determine which rows and cols needs to be zeroed
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0 # 0th row, different column value set to 0

                    if r>0: # if r is not 0, set that particular row, 0th column to 0
                        matrix[r][0] = 0
                    else: # else setting a separate Boolean variable to remember that the first row originally contained a zero and must eventually be zeroed.
                        rowZero = True
        
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[0][c]==0 or matrix[r][0]==0: # check if values in first row, different column is 0 OR values in first column, differnt row is 0, then change values of that particular row or column to 0; current column c has been marked for zeroing OR current row r has been marked for zeroing.
                    matrix[r][c] = 0
        
        if matrix[0][0] == 0: # if the first column of matrix is 0
            for r in range(ROWS): # iterate through that row
                matrix[r][0] = 0 # change every value in the row to 0 (first column 0)

        if rowZero: # if the first element of matrix is set to True
            for c in range(COLS): # iterate through that column
                matrix[0][c] = 0 # change every value in that column to 0 (first row 0)
                     