class Solution:
    def prefixesDivBy5(self, nums: list[int]) -> list[bool]:
        result = list()
        p = 0
        for n in nums:
            p = ((p << 1) + n) % 5
            result.append(p == 0)
        return result