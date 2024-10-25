"""
@complexity
time: O(log m + log n)
space: O(1)
"""


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        ROWS, COLS = len(matrix), len(matrix[0])
        l, r = 0, ROWS - 1
        while l <= r:
            m = (l + r) // 2
            if target > matrix[m][-1]:
                l = m + 1
            elif target < matrix[m][0]:
                r = m - 1
            else:
                break

        print(l, r)
        goodRow = (l + r) // 2
        print(f'good row: {goodRow}')

        l, r = 0, COLS - 1
        while l <= r:
            m = (l + r) // 2
            if target > matrix[goodRow][m]:
                l = m + 1
            elif target < matrix[goodRow][m]:
                r = m - 1
            else:
                return True

        return False
