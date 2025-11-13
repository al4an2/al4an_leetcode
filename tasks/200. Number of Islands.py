from typing import List, Iterator
class Solution: 
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        ans = 0

        def neighbors(r:int,c:int) -> Iterator[tuple[int,int]]:
            for dr, dc in ((-1,0), (1,0), (0,-1), (0,1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    yield nr, nc

        def dfs(start_r, start_c) -> None:
            stack = [(start_r, start_c)]

            while stack:
                r,c = stack.pop()
                if (r, c) in visited:
                    continue
                visited.add((r,c))

                for nr, nc in neighbors(r, c):
                    if grid[nr][nc] == "1" and (nr, nc) not in visited:
                        stack.append((nr, nc))

        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visited and grid[r][c] != "0":
                    dfs(r, c)
                    ans += 1
        return ans