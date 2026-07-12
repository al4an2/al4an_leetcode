class Solution:
    def maxArea(self, height: list[int]) -> int:
        start, finish = 0, len(height) - 1
        max_water = 0

        while start != finish:
            max_water = max(max_water, (finish - start) * min(height[start], height[finish]))
            if height[start] < height[finish]:
                start += 1
            else:
                finish -= 1

        return max_water