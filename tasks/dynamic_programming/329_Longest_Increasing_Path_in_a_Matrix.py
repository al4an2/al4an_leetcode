class Solution:
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]

        def dfs(i, j):
            if dp[i][j]:
                return dp[i][j]

            ans = 1

            num = matrix[i][j]
            ans = max(
                1 + dfs(i+1, j) if i+1 < m and num < matrix[i+1][j] else ans,
                1 + dfs(i, j+1) if j+1 < n and num < matrix[i][j+1] else ans,
                1 + dfs(i-1, j) if i-1 >= 0 and num < matrix[i-1][j] else ans,
                1 + dfs(i, j-1) if j-1 >= 0 and num < matrix[i][j-1] else ans,
            )

            dp[i][j] = ans
            return ans

        return max(dfs(i,j) for i in range(m) for j in range(n))