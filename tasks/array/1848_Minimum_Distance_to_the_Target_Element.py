class Solution:
    def getMinDistance(self, nums: list[int], target: int, start: int) -> int:
        min_dist = float('inf')
        for i, num in enumerate(nums):
            if num == target:
                min_dist = min(min_dist, abs(i - start))

        return 0 if min_dist == float('inf') else min_dist