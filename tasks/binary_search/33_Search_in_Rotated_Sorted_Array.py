class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right= 0, len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1
        
        pivot = left

        if target > nums[-1]:
            left, right = 0, pivot - 1
        else:
            left, right = pivot, len(nums) - 1
        
        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
