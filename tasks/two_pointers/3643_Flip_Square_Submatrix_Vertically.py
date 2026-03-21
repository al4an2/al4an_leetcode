class Solution:
    def reverseSubmatrix(self, grid: list[list[int]], x: int, y: int, k: int) -> list[list[int]]:
        upd_grid = [x[:] for x in grid]

        l, r = x, x+k-1
        end = y+k
        while l < r:
            upd_grid[l][y:end] = grid[r][y:end]
            upd_grid[r][y:end] = grid[l][y:end]
            l += 1
            r -= 1
        
        return upd_grid
            