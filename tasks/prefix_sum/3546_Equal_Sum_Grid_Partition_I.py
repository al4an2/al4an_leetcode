class Solution:
    def canPartitionGrid(self, grid: list[list[int]]) -> bool:
        m, n = len(grid), len(grid[0])

        row_sums = [0] * m
        col_sums = [0] * n
        total = 0

        for r in range(m):
            for c in range(n):
                val = grid[r][c]
                row_sums[r] += val
                col_sums[c] += val
                total += val

        if total % 2 != 0:
            return False

        prefix = 0
        for r in range(m - 1):
            prefix += row_sums[r]
            if prefix * 2 == total:
                return True

        prefix = 0
        for c in range(n - 1):
            prefix += col_sums[c]
            if prefix * 2 == total:
                return True

        return False
        