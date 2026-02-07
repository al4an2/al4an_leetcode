import math
class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:

        left, right = 1, max(piles)
        while left <= right:
            candidate = left + (right - left) // 2

            h_finish = 0
            for i in piles:

                h_finish += math.ceil(i / candidate)
            
            if h_finish <= h:
                right = candidate - 1
            else:
                left = candidate + 1
            
        return left