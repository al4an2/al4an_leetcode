class Solution:
    def maxDistance(self, colors: list[int]) -> int:
        visited = set()
        ans = 0

        for i in range(len(colors)):
            if colors[i] not in visited:
                visited.add(colors[i])
                for j in range(len(colors)-1, i, -1):
                    if colors[i] != colors[j]:
                        ans = max(ans, j - i)
                        break
        
        return ans

