import math

class Solution:
    def kLengthApart(self, nums: list[int], k: int) -> bool:
        last = -math.inf
        for i in range(len(nums)):
            if nums[i] == 1:
                if i - last - 1 < k:
                    return False
                last = i
        return True