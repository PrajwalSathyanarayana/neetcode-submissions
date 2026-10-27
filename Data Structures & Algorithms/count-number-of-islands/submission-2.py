class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0]) # initialize rows and columns
        islands = 0 # no. of islands
        directions = [[1,0],[-1,0],[0,1],[0,-1]] # 4 directions from a grid - move 1 cell down, up, right or left

        def dfs(r,c): # dfs on [r][c]
        # check if current row and column is out of bound, if the current row is greater than main ROW, and current column is greater than main COLS, if the current [row][column] is '0'
            if r<0 or c<0 or r>=ROWS or c>=COLS or grid[r][c] == '0': 
                return 
            grid[r][c] = '0'
            
            for dr, dc in directions:
                dfs(dr+r, dc+c)
        # end of dfs

        for r in range(ROWS): # iterate through rows
            for c in range(COLS): # itreate through columns
                if grid[r][c] == '1': # if the current position in grid is '1', call dfs on that grid position
                    dfs(r,c)
                    islands += 1 # increment the no. of islands

        return islands # return the no. of islands

# 
# 
#
# 
# 
# 
# 
# 
# 
# 
# 