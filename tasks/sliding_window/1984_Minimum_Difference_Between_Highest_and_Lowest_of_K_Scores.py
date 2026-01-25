class Solution:
    def minimumDifference(self, nums: list[int], k: int) -> int:
        if k == 1:
            return 0

        nums.sort()

        min_score = float("inf")

        for i in range(len(nums) - k+1):
            candidate = nums[i+k-1] - nums[i]
            min_score = min(min_score, candidate)
        
        return min_score
