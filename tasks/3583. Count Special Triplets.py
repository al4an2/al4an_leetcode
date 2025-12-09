class Solution:
    def specialTriplets(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        num_count = {}
        num_partial_count = {}

        for v in nums:
            num_count[v] = num_count.get(v, 0) + 1

        result = 0
        for v in nums:
            target = v * 2
            left = num_partial_count.get(target, 0)
            num_partial_count[v] = num_partial_count.get(v, 0) + 1
            right = num_count.get(target, 0) - num_partial_count.get(target, 0)
            result = (result + left * right) % MOD

        return result
