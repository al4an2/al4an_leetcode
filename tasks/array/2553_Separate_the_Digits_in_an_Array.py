class Solution:
    def separateDigits(self, nums: list[int]) -> list[int]:
        ans = []
        for n in nums:
            for x in str(n):
                ans.append(int(x))
        return ans