class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque() # initialize deque
        time, fresh = 0, 0 # variables to keep track of time and no. of fresh fruit

        ROWS, COLS = len(grid), len(grid[0]) # initialize rows, cols

        for r in range(ROWS): # iterate through every row
            for c in range(COLS): # iterate through every column
                if grid[r][c] == 1: # if a grid co-ordinate is 1 i.e,, fresh fruit
                    fresh += 1 # increment fresh by 1
                if grid[r][c] == 2: # if a grid co-ordinate is 2 i.e., rotten fruit
                    q.append([r,c]) # add the co-ordinate (r,c) to deque
        
        directions = [[1,0],[-1,0],[0,1],[0,-1]] # 4 adjacent directions

        while q and fresh>0: # q is not empty and fresh > 0

            for i in range(len(q)): # iterate through the deque
                r,c = q.popleft() # remove the co-ordinate (r,c)
                for dr, dc in directions: # iterate through the direction list
                    row, col = dr + r, dc + c # adjacent row and column
                    # if (row, col) is out of bounds or rotten or empty, continue to next iteration 
                    if((row < 0 or row >= ROWS) or 
                    (col < 0 or col >= COLS) or 
                    (grid[row][col] != 1)):
                        continue
                    grid[row][col] = 2 # update (row, col) to rotten i.e., 2
                    q.append([row, col]) # append the new (row, col) to deque
                    fresh -= 1 # decrement fresh by 1, since (row, col) got updated to 2
            time += 1   # one entire loop is completed, hence time has to be incremented by 1

        return time if fresh == 0 else -1 # return time if every fruit is rotten (fresh == 0), else return -1