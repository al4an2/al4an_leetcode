class Solution:
    def minimumCost(self, nums: list[int]) -> int:
        if len(nums) == 3:
            return sum(nums)
        
        arr = sorted(nums[1:])
        return nums[0] + arr[0] + arr[1]