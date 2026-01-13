class Solution:
    def separateSquares(self, squares: list[list[int]]) -> float:

        def area_below(pivot,squares):
            lower_part = 0.0
            for x,y,li in squares:

                roof = y + li
                if roof <= pivot:
                    lower_part += li**2
                if y < pivot < roof:
                    square_high = pivot - y
                    lower_part += li * square_high

            return lower_part

        total_area = sum(el[2]**2 for el in squares)

        low = float(min(el[1] for el in squares))
        high = float(max(el[1]+el[2] for el in squares))
        eps = 1e-6

        while (high - low) > eps:
            pivot = (low+high)/2

            if area_below(pivot,squares) * 2 >= total_area:
                high = pivot
            else:
                low = pivot
            

        return low

            