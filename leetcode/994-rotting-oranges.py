"""
@complexity
time: O(n)
space: O(n)
"""


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()

        def isValid(i, j):
            return 0 <= i < ROWS and 0 <= j < COLS and grid[i][j] == 1

        fresh = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))
                elif grid[i][j] == 1:
                    fresh += 1

        if fresh == 0:
            return 0

        minutes = 0
        while queue:
            x, y, time = queue.popleft()
            minutes = max(minutes, time)

            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy
                if isValid(new_x, new_y):
                    grid[new_x][new_y] = 2
                    fresh -= 1
                    queue.append((new_x, new_y, time + 1))

        return minutes if fresh == 0 else -1
