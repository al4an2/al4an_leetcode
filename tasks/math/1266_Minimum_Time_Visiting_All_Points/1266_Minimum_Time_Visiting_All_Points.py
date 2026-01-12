class Solution:
    def minTimeToVisitAllPoints(self, points: list[list[int]]) -> int:
        
        ans = 0 

        for i in range(len(points)-1):
            xi,yi = points[i]
            xj,yj = points[i+1]
            ans += max(abs(xj - xi), abs(yj - yi)) #chebyshev_distance

        return ans