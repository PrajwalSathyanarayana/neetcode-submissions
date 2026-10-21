class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l, r = 0, len(matrix)-1 # 2 pointers left and right

        while l<r: # l is in bound with r i.e., l<r => loop runs
            for i in range(r-l): # i ranges from 0 to r-l
                top, bottom = l, r  # 2 pointers top and bottom

                topLeft = matrix[top][l+i] # save the top left value in temp variable

                matrix[top][l+i] = matrix[bottom-i][l] # move bottom left to top left

                matrix[bottom-i][l] = matrix[bottom][r-i] # move bottom right to bottom left

                matrix[bottom][r-i] = matrix[top+i][r] # move top right to bottom right

                matrix[top+i][r] = topLeft # move top left to top right
             
            l += 1; # move left pointer to right,
            r -= 1; # move right pointer down
            
           
        
