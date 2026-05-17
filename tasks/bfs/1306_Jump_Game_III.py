from collections import deque

class Solution:
    def canReach(self, arr: list[int], start: int) -> bool:
        n = len(arr)
        queue = deque()
        visited = set()

        queue.append(start)

        while queue:
            index = queue.popleft()
            value = arr[index]

            if value == 0:
                return True

            jump_left = index - value
            jump_right = index + value
            if jump_left >= 0 and jump_left not in visited:
                queue.append(jump_left)
                visited.add(index)
                
            if jump_right < n and jump_right not in visited:
                queue.append(jump_right)
                visited.add(index)

        return False