class Solution:
    def maxMatrixSum(self, matrix: list[list[int]]) -> int:
        total_sum = 0
        min_abs_value = float("inf")
        negative_count = 0

        for row in matrix:
            for val in row:
                total_sum += abs(val)
                if val < 0:
                    negative_count += 1
                min_abs_value = min(min_abs_value, abs(val))

        if negative_count % 2 != 0:
            total_sum -= 2 * min_abs_value
        
        return total_sum