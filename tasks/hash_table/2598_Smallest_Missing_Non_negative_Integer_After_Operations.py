from collections import defaultdict

class Solution:
    def findSmallestInteger(self, nums: list[int], value: int) -> int:
        hash_table = defaultdict(int)
        for n in nums:
            hash_table[n % value] += 1

        mex = 0
        while hash_table[mex % value] > 0:
            hash_table[mex % value] -= 1
            mex += 1

        return mex
