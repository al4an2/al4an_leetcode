class Solution:
    def maxProductPath(self, grid: list[list[int]]) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])
        max_dp = [[0]* n for _ in range(m)]
        min_dp = [[0]* n for _ in range(m)]

        max_dp[0][0] = min_dp[0][0] = grid[0][0]

        for i in range(1,m):
            max_dp[i][0] = min_dp[i][0] = max_dp[i-1][0] * grid[i][0]

        for i in range(1,n):
            max_dp[0][i] = min_dp[0][i] = max_dp[0][i-1] * grid[0][i]

        for i in range(1,m):
            for j in range(1,n):

                candidates = [
                    max_dp[i-1][j] * grid[i][j],
                    max_dp[i][j-1] * grid[i][j],
                    min_dp[i-1][j] * grid[i][j],
                    min_dp[i][j-1] * grid[i][j],
                ]

                max_dp[i][j] = max(candidates)
                min_dp[i][j] = min(candidates)
            
        ans = max_dp[m-1][n-1]
        return -1 if ans < 0 else ans % MOD