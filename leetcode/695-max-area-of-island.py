"""
@complexity
time: O(m * n)
space: O(m * n)
"""


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        ROWS, COLS = len(grid), len(grid[0])

        def isValid(i, j):
            return 0 <= i < ROWS and 0 <= j < COLS and grid[i][j] == 1

        def dfs(i, j):
            stack = [(i, j)]
            grid[i][j] = 0
            current_area = 1

            while stack:
                x, y = stack.pop()
                for dx, dy in directions:
                    new_x, new_y = x + dx, y + dy
                    if isValid(new_x, new_y):
                        stack.append((new_x, new_y))
                        grid[new_x][new_y] = 0
                        current_area += 1

            return current_area

        maximum_area = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    maximum_area = max(maximum_area, dfs(i, j))

        return maximum_area
