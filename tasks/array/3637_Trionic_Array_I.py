class Solution:
    def isTrionic(self, nums: list[int]) -> bool:
        if nums[1] <= nums[0]:
            return False

        change = 0
        for i in range(2, len(nums)):
            if nums[i] == nums[i-1]:
                return False
            if nums[i] < nums[i-1] > nums[i-2] or nums[i] > nums[i-1] < nums[i-2]:
                change += 1
            
            if change > 2:
                return False

        return change == 2