class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols, squares = collections.defaultdict(set), collections.defaultdict(set), collections.defaultdict(set)
        # hashmap for rows, cols, and 3*3 sub grids(squares = {(r//3, c//3):duplicates}

        for r in range(9): # iterate through each row
            for c in range(9): # iterate through each column
                if board[r][c] == '.': # if current (r,c) is empty => continue (skip it)
                    continue
                if (board[r][c] in rows[r] or # current (r,c) value in row hashmap
                board[r][c] in cols[c] or # current (r,c) value in column hashmap
                board[r][c] in squares[(r//3, c//3)]): # current(r,c) value in 3*3 subgrid
                    return False # means duplicates => return False
                # else, duplicate not found, add current (r,c) value to three hashmaps
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r//3, c//3)].add(board[r][c])

        return True