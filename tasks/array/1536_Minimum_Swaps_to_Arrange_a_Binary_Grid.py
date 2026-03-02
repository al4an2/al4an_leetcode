class Solution:
    def minSwaps(self, grid: list[list[int]]) -> int:
        n = len(grid)
        swaps = 0
        num_z = []
        for i in range(n):
            res = 0
            for j in reversed(grid[i]):
                if j == 0:
                    res += 1
                else:
                    break
            num_z.append(res)
        
        for idx in range(n):
            need = n - idx - 1

            if num_z[idx] >= need:
                continue

            j = idx  
            while j < n and num_z[j] < need:
                j += 1
            
            if j == n:
                return -1
            
            while j > idx:
                num_z[j], num_z[j - 1] = num_z[j - 1], num_z[j]
                swaps += 1
                j -= 1

        return swaps
