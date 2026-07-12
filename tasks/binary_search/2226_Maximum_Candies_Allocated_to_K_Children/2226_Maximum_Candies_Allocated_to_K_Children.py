class Solution:
    def maximumCandies(self, candies: list[int], k: int) -> int:
        def solve(candies, k, val):
            total_pieces = sum(candy // val for candy in candies if val <= candy)
            return total_pieces >= k

        if sum(candies) < k:
            return 0

        candies.sort()
        left, right = 1, max(candies)
        answer = 0

        while left <= right:
            mid = (left + right) // 2
            if solve(candies, k, mid):
                answer = mid
                left = mid + 1
            else:
                right = mid - 1
        
        return answer


