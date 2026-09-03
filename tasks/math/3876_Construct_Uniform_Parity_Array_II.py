class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        min_n = min(nums1)

        return min_n % 2 == 1 or all(x % 2 == 0 for x in nums1)

#another decision
class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        min_n = min(nums1)
        has_odd = False

        for num in nums1:
            if num % 2 == 1:
                has_odd = True
                break

        return min_n % 2 == 1 or not has_odd