class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: list[int], vBars: list[int]) -> int:
        h_max = 1
        v_max = 1

        hBars.sort()
        vBars.sort()

        counter_i,counter_j = 1, 1
        for i in range(len(hBars) - 1):
            if hBars[i+1] - hBars[i] == 1:
                counter_i += 1
                h_max = max(counter_i, h_max)
            else:
                counter_i = 1

        for j in range(len(vBars) - 1):
            if vBars[j+1] - vBars[j] == 1:
                counter_j += 1
                v_max = max(counter_j, v_max)
            else:
                counter_j = 1

        min_rem = min((h_max), (v_max))
        return (min_rem+1)**2