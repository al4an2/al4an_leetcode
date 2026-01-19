class Solution:
    def maxSideLength(self, mat: list[list[int]], threshold: int) -> int:
        m, n= len(mat), len(mat[0])
        prefix_sum = [[0] * (n+1) for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                prefix_sum[i][j] = (
                    prefix_sum[i][j-1]
                    + prefix_sum[i-1][j] 
                    + mat[i-1][j-1] 
                    - prefix_sum[i-1][j-1]
                    )

        def check(k):
            for i in range(m - k + 1):
                for j in range(n - k + 1):
                    total = (
                        prefix_sum[i+k][j+k] 
                        - prefix_sum[i][j+k] 
                        - prefix_sum[i+k][j] 
                        + prefix_sum[i][j]
                        )
                    if total <= threshold:
                        return True
            return False

        
        left,right = 1, min(m,n)
        ans = 0
        while left <= right:
            mid = (left + right) // 2 
            if check(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        
        return ans