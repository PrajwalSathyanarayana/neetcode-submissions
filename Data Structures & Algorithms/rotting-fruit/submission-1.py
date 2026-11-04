class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # BFS => deque()
        q=deque() # double ended queue
        time, fresh = 0,0 # total time, fresh fruits
        ROWS, COLS = len(grid), len(grid[0]) # no. of rows, cols
        # iterate through each row and column and find the no. of fresh fruits, add the rotten fruit to deque
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==1:
                    fresh += 1
                if grid[r][c]==2:
                    q.append([r,c])
        # 4 directions from current grid position - right, left, down, up
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        # deque is not empty and fresh fruits still exist
        while q and fresh>0:
        # iterate through the current deque and pop the current [r,c]
            for i in range(len(q)):
                r,c = q.popleft()
        # iterate through 4 directions from the current grid cell
                for dr, dc in directions:
                    row=r+dr; col=c+dc
            # if current cell is invalid or isnt a fresh fruit, ignore it and move on to next neighbor
                    if ((row<0 or row>=ROWS) or
                    (col<0 or col>=COLS) or 
                    grid[row][col] != 1):
                        continue
                    grid[row][col]=2 # adjacent fruit gets rotten
                    q.append([row,col]) # append the (row,col) to deque
                    fresh -= 1 # decrement fresh fruit by 1
            time += 1 # increase time by 1
        return time if fresh==0 else -1 # return time if there are no fresh fruits, else, return -1
                    
                