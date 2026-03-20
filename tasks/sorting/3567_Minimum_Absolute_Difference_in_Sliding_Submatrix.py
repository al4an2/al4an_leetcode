class Solution:
    def minAbsDiff(self, grid: list[list[int]], k: int) -> list[list[int]]:
        
        m, n = len(grid), len(grid[0])
        res = [[0] * (n - k+1) for _ in range(m - k+1)]
        
        for row in range(m - k+1):
            for col in range(n - k+1):
                vals = []

                for r in range(row, row + k):
                    for c in range(col, col + k):
                        vals.append(grid[r][c])

                vals.sort()

                max_d = float('inf')
                for idx in range(1, len(vals)):
                    if vals[idx] != vals[idx-1]:
                        max_d = min(max_d, vals[idx] - vals[idx-1])

                res[row][col] = max_d if max_d != float('inf') else 0
        return res
                

                
                