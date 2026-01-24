class Solution:
    def minPairSum(self, nums: list[int]) -> int:
        cur_max = 0
        nums.sort()
        left, right = 0, len(nums) - 1
        while left < right:
            candidate = nums[left] + nums[right]
            cur_max = max(cur_max, candidate)
            left += 1
            right -= 1
        return cur_max