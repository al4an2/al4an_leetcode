class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        count = 0
        m = len(grid[0])
        for i in range(len(grid)):
            left, right = 0, m-1
            first_neg = m

            while left <= right:
                mid = (left+right) // 2

                if grid[i][mid] < 0:
                    right = mid-1
                    first_neg = mid
                    
                else:
                    left = mid+1

            count += m - first_neg

        return count