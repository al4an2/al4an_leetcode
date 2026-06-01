class Solution:
    def minimumCost(self, cost: list[int]) -> int:
        cost.sort()
        ans = 0

        for i in range(len(cost)-1, -1, -1):
            if i % 3 != 2:
                ans += cost[i]

        return ans


