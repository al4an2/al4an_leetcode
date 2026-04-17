class Solution:
    def minMirrorPairDistance(self, nums: list[int]) -> int:
        ans = float('inf')
        reserved_d = dict()
        for i, num in enumerate(nums):
            if num in reserved_d:
                ans = min(ans, i - reserved_d[num])
            reserved_d[int(str(num)[::-1])] = i
    
        return -1 if ans == float('inf') else ans

