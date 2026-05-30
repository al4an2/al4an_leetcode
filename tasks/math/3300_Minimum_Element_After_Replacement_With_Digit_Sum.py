class Solution:
    def minElement(self, nums: list[int]) -> int:
        ans = float("inf")
        for el in nums:
            candidate = 0

            while el > 0:
                candidate += el % 10
                el //=10
            ans = min(ans, candidate)

        return ans