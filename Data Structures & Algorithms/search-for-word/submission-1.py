class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0]) # initialize rows and columns
        path = set() # set to keep track of visited nodes

        def dfs(r,c,i): # helper function
            if i == len(word): # if the position i in word == len(word)
                return True # return True
            if (( r< 0 or c < 0) # rows and columns out of bound 
            or (r >= ROWS or c >= COLS) # rows >= no. of rows in board, cols >= no. of cols in board
            or ((r,c) in path)  # grid (r,c) being revisited twice
            or word[i] != board[r][c]): # character in word at position i != character in board at (r,c)
                return False # return False 
            
            path.add((r,c)) # adding visited node (r,c) to path set
            res =  (dfs(r+1,c,i+1) or dfs(r-1,c,i+1) or # move row wise
                    dfs(r,c+1,i+1) or dfs(r,c-1,i+1)) # move column wise
            path.remove((r,c)) # remove the visited node from set so that it wont be visited again
            return res # return res (need one of the condition in res to be true)

        # iterate through each and every starting position on the board 
        for r in range(ROWS): 
            for c in range(COLS):
                if dfs(r,c,0): # pass the default starting parameters to the helper function
                    return True
        return False
