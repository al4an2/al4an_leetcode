class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        n = len(nums)
        dp = nums[0]
        max_sum = nums[0]

        for i in range(1, n):
            dp = max(nums[i] + dp, nums[i])
            max_sum = max(max_sum, dp)
    
        return max_sum
            
