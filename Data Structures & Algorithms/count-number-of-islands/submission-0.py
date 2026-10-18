class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid: # if the grid is empty, then return 0
            return 0
        
        rows, cols = len(grid), len(grid[0]) # initialize rows and columns
        visit = set() # keep track of visited positions
        islands = 0 # keeppp track of no. of islands
       
        def bfs(r,c): # BFS is an iterative algorithm, hence using a deque
            q = collections.deque() # create a deque
            visit.add((r,c)) # add the co-ordinate (r,c) to visit set
            q.append((r,c)) # append the co-ordinate (r,c) to deque q

            while q:
                row, col = q.popleft() # pop the co-ordinate from left of the deque
                directions = [[1,0],[-1,0],[0,1],[0,-1]] # 4 postions that can be visited from the current co-ordinate (r,c) i.e., north, south, east, west
                for dr, dc in directions: # iterate through the directions list
                    r,c = row+dr, col+dc # row + dr (1,-1,0,0) // col + dc (0,0,1,-1)
                    if ((r) in range(rows) and # check if r is in bound of total rows
                    (c) in range(cols) and # check if c is in bound of total cols
                    grid[r][c] == '1' and # if the current co-ordinate (r,c) = '1'
                    (r, c) not in visit): # current co-ordinate (r,c) is not visited
                        q.append((r, c)) # then append co-ordinate(r,c) to q
                        visit.add((r, c)) # append co-ordinate(r,c) to visit

        for r in range(rows): # iterate through each row
            for c in range(cols): # iterate throgh each column
                if grid [r][c] == '1' and (r,c) not in visit: # if the encountered grid[r][c] is 1 and the co-ordinate (r,c) is not in visited set
                    bfs(r,c) # call bfs helper function
                    islands += 1 # increment the no. of islands
        return islands
