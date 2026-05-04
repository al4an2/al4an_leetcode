import math

class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        size = len(matrix) - 1
        n, m = math.ceil(len(matrix)/2), math.floor(len(matrix)/2)
        

        for i in range(n):
            for j in range(m):
                el, matrix[j][size-i] = matrix[j][size-i], matrix[i][j]
                el, matrix[size-i][size-j] = matrix[size-i][size-j], el
                el, matrix[size-j][i] = matrix[size-j][i], el
                matrix[i][j] = el
                