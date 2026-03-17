class Solution:
    def largestSubmatrix(self, matrix: list[list[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        prev_row = [0] * n
        res = 0

        for row in range(m):
            current_row = matrix[row]
            for col in range(n):
                if current_row[col] != 0:
                    current_row[col] += prev_row[col]
            sorted_row = sorted(current_row, reverse = True)

            for idx in range(n):
                res = max(res, sorted_row[idx] * (idx + 1))

            prev_row = current_row

        return res