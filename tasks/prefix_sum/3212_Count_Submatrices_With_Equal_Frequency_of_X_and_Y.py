class Solution:
    def numberOfSubmatrices(self, grid: list[list[str]]) -> int:
        def helper(ch: str) -> tuple[int, int]:
            if ch == "X":
                return 1, 1
            if ch == "Y":
                return -1, 0
            return 0, 0

        m, n = len(grid), len(grid[0])
        res = 0

        p_sum = [[0] * n for _ in range(m)]
        xcnt = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                balance, x = helper(grid[i][j])

                if i > 0:
                    balance += p_sum[i - 1][j]
                    x += xcnt[i - 1][j]
                if j > 0:
                    balance += p_sum[i][j - 1]
                    x += xcnt[i][j - 1]
                if i > 0 and j > 0:
                    balance -= p_sum[i - 1][j - 1]
                    x -= xcnt[i - 1][j - 1]

                p_sum[i][j] = balance
                xcnt[i][j] = x

                if balance == 0 and x > 0:
                    res += 1

        return res