class Solution:
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        n,m = len(matrix), len(matrix[0])
        dp = [0] * m
        max_area = 0

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == "1":
                    dp[j] += 1
                else:
                    dp[j] = 0
            
            stack = []
            for j in range(m + 1):   
                cur_height = dp[j] if j < m else 0
                while stack and cur_height < dp[stack[-1]]:
                    h = dp[stack.pop()]
                    w = j if not stack else j - stack[-1] - 1
                    max_area = max(max_area, h * w)
                stack.append(j)

        return max_area