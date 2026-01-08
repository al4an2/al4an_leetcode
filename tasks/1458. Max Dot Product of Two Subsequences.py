class Solution:
    def maxDotProduct(self, nums1: list[int], nums2: list[int]) -> int:
        n, m = len(nums1), len(nums2)

        dp = [[0] * m for _ in range(n)]

        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                pair = nums1[i] * nums2[j]

                if i+1 < n and j+1 < m:
                    pair += dp[i+1][j+1]
                
                skip_i = dp[i+1][j] if i+1 < n else float('-inf')
                skip_j = dp[i][j+1] if j+1 < m else float('-inf')

                dp[i][j] = max(pair, skip_i, skip_j, nums1[i]*nums2[j])
        
        return dp[0][0]