
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        # ROWS = 4, COLS = 5

        islands = 0
        # Initially islands = 0

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        # Down, Up, Right, Left

        def dfs(r, c):
            # Base case: stop if out of bounds or water ('0').
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS
                    or grid[r][c] == '0'):
                return

            # We found unvisited land.
            # Mark it visited so we don't count it again.
            grid[r][c] = '0'

            # Explore all 4 directions, in order.
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        # Outer loop scans the entire grid.
        for r in range(ROWS):
            for c in range(COLS):

                # First land found at (0, 1).
                if grid[r][c] == '1':
                    dfs(r, c)

                    # DFS has finished exploring this entire island.
                    islands += 1

        return islands


# INPUT:
# 0 1 1 1 0
# 0 1 0 1 0
# 1 1 0 0 0
# 0 0 0 0 0

# INITIAL STATE:
# ROWS = 4, COLS = 5, islands = 0

# OUTER LOOP:
# (0,0) = '0' -> skip
# (0,1) = '1' -> call dfs(0,1)

# COMPLETE DFS TRACE
#
# dfs(0,1): mark (0,1) = '0'
#   DOWN -> dfs(1,1)
#     dfs(1,1): mark (1,1) = '0'
#       DOWN -> dfs(2,1)
#         dfs(2,1): mark (2,1) = '0'
#           DOWN -> dfs(3,1): water, return
#           UP   -> dfs(1,1): visited, return
#           RIGHT-> dfs(2,2): water, return
#           LEFT -> dfs(2,0)
#             dfs(2,0): mark (2,0) = '0'
#               DOWN -> dfs(3,0): water, return
#               UP   -> dfs(1,0): water, return
#               RIGHT-> dfs(2,1): visited, return
#               LEFT -> dfs(2,-1): out of bounds, return
#             dfs(2,0) finishes
#         dfs(2,1) finishes
#       UP   -> dfs(0,1): visited, return
#       RIGHT-> dfs(1,2): water, return
#       LEFT -> dfs(1,0): water, return
#     dfs(1,1) finishes
#
#   UP -> dfs(-1,1): out of bounds, return
#   RIGHT -> dfs(0,2)
#     dfs(0,2): mark (0,2) = '0'
#       DOWN -> dfs(1,2): water, return
#       UP   -> dfs(-1,2): out of bounds, return
#       RIGHT-> dfs(0,3)
#         dfs(0,3): mark (0,3) = '0'
#           DOWN -> dfs(1,3)
#             dfs(1,3): mark (1,3) = '0'
#               DOWN -> dfs(2,3): water, return
#               UP   -> dfs(0,3): visited, return
#               RIGHT-> dfs(1,4): water, return
#               LEFT -> dfs(1,2): water, return
#             dfs(1,3) finishes
#           UP   -> dfs(-1,3): out of bounds, return
#           RIGHT-> dfs(0,4): water, return
#           LEFT -> dfs(0,2): visited, return
#         dfs(0,3) finishes
#       LEFT -> dfs(0,1): visited, return
#     dfs(0,2) finishes
#   LEFT -> dfs(0,0): water, return
# dfs(0,1) finishes
#
# DFS has now visited all 7 land cells:
# (0,1), (1,1), (2,1), (2,0), (0,2), (0,3), (1,3)
#
# Return to the outer loop:
# islands += 1 -> islands = 1
#
# Continue scanning:
# (0,2), (0,3), (1,1), (1,3), (2,0), (2,1)
# are all now '0', so no additional DFS starts.
#
# All cells in row 3 are also water.
#
# FINAL RESULT:
# return 1