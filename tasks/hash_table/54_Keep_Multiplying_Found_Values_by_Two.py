from typing import List

class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        set_n = set(nums)
        while original in set_n:
            original *= 2
        return original