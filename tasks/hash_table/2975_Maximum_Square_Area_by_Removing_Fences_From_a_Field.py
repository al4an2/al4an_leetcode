class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: list[int], vFences: list[int]) -> int:
        h = [1] + hFences + [m]
        v = [1] + vFences + [n]
        max_side = 0
        h.sort()
        v.sort()
        MOD = 10**9+7

        height = set()
        for i in range(len(h)):
            for j in range(i+1,len(h)):
                height.add(h[j] - h[i])
        
        for i in range(len(v)):
            for j in range(i+1,len(v)):
                d = v[j] - v[i]
                if d in height:
                    max_side = max(max_side,d)

        return max_side**2%MOD if max_side > 0 else -1