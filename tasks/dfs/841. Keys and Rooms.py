class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        visited = set()
        def dfs(r):
            visited.add(r)
            for i in rooms[r]:
                if i not in visited:
                    dfs(i)
        
        dfs(0)

        return len(rooms) == len(visited)

