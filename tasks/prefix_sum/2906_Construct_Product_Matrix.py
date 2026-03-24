class Solution:
    def constructProductMatrix(self, grid: list[list[int]]) -> list[list[int]]:
        MOD = 12345

        flat = [x for row in grid for x in row]
        total = len(flat)

        prefix = [1] * total
        suffix = [1] * total

        for i in range(1, total):
            prefix[i] = prefix[i - 1] * flat[i - 1] % MOD

        for i in range(total - 2, -1, -1):
            suffix[i] = suffix[i + 1] * flat[i + 1] % MOD

        rows = len(grid)
        cols = len(grid[0])
        ans = [[0] * cols for _ in range(rows)]

        for r in range(rows):
            for c in range(cols):
                pos = r * cols + c
                ans[r][c] = prefix[pos] * suffix[pos] % MOD

        return ans