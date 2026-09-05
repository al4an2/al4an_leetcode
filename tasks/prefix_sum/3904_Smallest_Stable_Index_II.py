class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        suffix = [0] * n

        suffix[-1] = nums[-1]
        for i in range(n-2, -1, -1):
            suffix[i] = min(nums[i], suffix[i+1])

        max_n = nums[0]
        for j in range(n):
            max_n = max(nums[j], max_n)

            if max_n - suffix[j] <= k:
                return j

        return -1