class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        left, right = 0, rows * cols - 1

        while left <= right:
            mid = left + (right - left) // 2

            row = mid // cols
            col = mid % cols

            value = matrix[row][col]
            
            if value < target:
                left = mid + 1
            elif value > target:
                right = mid - 1
            else:
                return True

        return False