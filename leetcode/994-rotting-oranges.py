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

        fresh = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1

        def isValid(i, j):
            return 0 <= i < ROWS and 0 <= j < COLS and grid[i][j] == 1

        if fresh == 0:
            return 0

        time = 0
        while queue and fresh:
            for _ in range(len(queue)):
                i, j = queue.popleft()
                for di, dj in directions:
                    new_i, new_j = i + di, j + dj
                    if isValid(new_i, new_j):
                        grid[new_i][new_j] = 2
                        fresh -= 1
                        queue.append((new_i, new_j))

            time += 1

        return time if fresh == 0 else -1
