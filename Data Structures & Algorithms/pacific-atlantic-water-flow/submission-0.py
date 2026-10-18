class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        def dfs(r, c, visit, prevHeight): # recursive DFS
            if(((r,c) in visit) or # check if (r,c) is already visited or not
            (r<0 or c<0) or # if the rows and columns are in bound
            (r == rows or c == cols) or # if the current (r,c) == rows, cols
            (heights[r][c] < prevHeight)): # if the value of particular (r,c) < previous value
                return

            visit.add((r,c)) # add current (r,c) to set()

            # recursive DFS in 4 diections (top, bottom, left, right from the current (r,c))
            dfs(r+1, c, visit, heights[r][c]) # top
            dfs(r-1, c, visit, heights[r][c]) # bottom
            dfs(r, c+1, visit, heights[r][c]) # right
            dfs(r, c-1, visit, heights[r][c]) # left


        rows, cols = len(heights), len(heights[0]) # initialize the rows, cols
        pac, atl = set(), set() # 2 sets for keeping track of visited co-ordinates

        for c in range(cols): # pacific
            dfs(0, c, pac, heights[0][c]) # top row (0th row), particular column, pacific set, prevHeight[0][c]
            dfs(rows-1, c, atl, heights[rows-1][c]) # bottom row (rows-1), particular column, atlantic set, prevHeight[rows-1][c]
        for r in range(rows): # pacificAtlantic
            dfs(r, 0, pac, heights[r][0]) # particular row, left column (0th column), pacific set, prevHeight[r][0]
            dfs(r, cols-1, atl, heights[r][cols-1]) # particular row, right column (cols-1), atlantic set, prevHeight[r][cols-1]

        res = [] # list to store the common co-ordinates

        for r in range(rows): # iterate through each row
            for c in range(cols): # iterate through each col
                if (r,c) in pac and (r,c) in atl: # if co-ordinate is in both pac() and atl()
                    res.append([r,c]) # append the co-ordinate to result set
        
        return res # return result