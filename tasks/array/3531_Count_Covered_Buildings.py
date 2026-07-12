class Solution:
    def countCoveredBuildings(self, n: int, buildings: list[list[int]]) -> int:
        max_x = [0] * (n + 1)
        min_x = [n + 1] * (n + 1)
        max_y = [0] * (n + 1)
        min_y = [n + 1] * (n + 1)

        for x, y in buildings:
            min_x[y] = min(min_x[y], x)
            min_y[x] = min(min_y[x], y)
            max_x[y] = max(max_x[y], x)
            max_y[x] = max(max_y[x], y)

        res = 0
        for x, y in buildings:
            if (
                x > min_x[y]
                and x < max_x[y]
                and y > min_y[x]
                and y < max_y[x]
            ):
                res += 1

        return res