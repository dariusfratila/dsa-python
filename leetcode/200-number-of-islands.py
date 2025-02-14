"""
@complexity
time: O(m * n)
space: O(m * n)
"""


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        ROWS, COLS = len(grid), len(grid[0])

        def is_valid(i, j):
            return 0 <= i < ROWS and 0 <= j < COLS and grid[i][j] == '1'

        def dfs(i, j):
            stack = [(i, j)]

            while stack:
                x, y = stack.pop()
                grid[x][y] = '0'
                for dx, dy in directions:
                    new_x, new_y = x + dx, y + dy
                    if is_valid(new_x, new_y):
                        stack.append((new_x, new_y))

        num_islands = 0
        for i in range(ROWS):
            for j in range(COLS):
                if is_valid(i, j):
                    num_islands += 1
                    dfs(i, j)

        return num_islands
