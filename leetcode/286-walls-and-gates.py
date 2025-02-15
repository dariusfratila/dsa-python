"""
@complexity
time: O(n)
space: O(n)
"""


class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        def isValid(i, j):
            return 0 <= i < ROWS and 0 <= j < COLS and grid[i][j] == INF

        ROWS, COLS = len(grid), len(grid[0])
        INF = 2147483647

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        queue = deque()

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    queue.append((i, j, 0))

        while queue:
            i, j, value = queue.popleft()

            for di, dj in directions:
                new_i, new_j = i + di, j + dj
                if isValid(new_i, new_j):
                    grid[new_i][new_j] = value + 1
                    queue.append((new_i, new_j, value + 1))
