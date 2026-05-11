class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        nums_1 = set(nums1)
        nums_2 = set(nums2)

        return list(nums_1.intersection(nums_2))