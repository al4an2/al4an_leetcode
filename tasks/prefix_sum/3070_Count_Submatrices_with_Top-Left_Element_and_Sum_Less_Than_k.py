class Solution:
    def countSubmatrices(self, grid: list[list[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        res = 0

        p_sum = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                p_sum[i][j] = grid[i][j]

                if i > 0:
                    p_sum[i][j] += p_sum[i-1][j]
                if j > 0:
                    p_sum[i][j] += p_sum[i][j-1]
                if i > 0 and j > 0:
                    p_sum[i][j] -= p_sum[i-1][j-1]
                
                if p_sum[i][j] <= k:
                    res += 1
                else:
                    break

        return res