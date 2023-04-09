class Solution:
    def numIslands(self, grid):

        visited = set() # x, y
        ROWS = len(grid)
        COLS = len(grid[0])

        def dfs(row, col):
            # check if out of bounds
            if (row < 0 or
                col < 0 or
                row >= ROWS or
                col >= COLS or
                (row, col) in visited or
                grid[row][col] != '1'):
                return

            visited.add((row, col))
            dfs(row, col + 1)
            dfs(row, col - 1)
            dfs(row - 1, col)
            dfs(row + 1, col)

        count = 0
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == '1' and (row, col) not in visited:
                    dfs(row, col)
                    count += 1
        return count