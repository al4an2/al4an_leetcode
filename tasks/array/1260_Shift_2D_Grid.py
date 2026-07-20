class Solution:
    def shiftGrid(self, grid: list[list[int]], k: int) -> list[list[int]]:
        flat_list = [val for row in grid for val in row]
        size = len(grid[0])
        k = k % len(flat_list)

        flat_list = flat_list[-k:] + flat_list[:-k]
        
        return [flat_list[i : i + size] for i in range(0, len(flat_list), size)]
            
