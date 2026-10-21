class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = [] # result array
        l, r = 0, len(matrix[0]) # 0, no of cols
        t, b = 0, len(matrix) # 0, no of rows

        while l<r and t<b: # check if pointers are in bound => execute loop

            # get every value in top row
            for i in range(l, r): # iterate from left to right
                res.append(matrix[t][i]) # top row, each value from column
            t += 1  # shift top pointer by 1 towards bottom
            
            # get every value in right column
            for i in range(t, b): # iterate from top to bottom
                res.append(matrix[i][r-1]) # each value from row, right column
            r -=1 # shift right pointer by 1 towards left
            
            if not (l<r and t<b):
                break 

            # get every value in bottom row
            for i in range(r-1, l-1, -1): # iterate from right to left (reverse)
                res.append(matrix[b-1][i]) # bottom row, each value from column
            b -= 1 # shift bottom pointer by 1 towards top

            # get every value in left column
            for i in range(b-1, t-1, -1): # iterate from bottom to top (reverse)
                res.append(matrix[i][l]) # each value from row, left column
            l += 1

        return res