from collections import deque, defaultdict

class Solution:
    def minJumps(self, arr: list[int]) -> int:
        target = len(arr) - 1

        if target == 0:
            return 0

        queue = deque([(0, 0)])
        visited = {0}

        value_to_idxs = defaultdict(list)

        for i, v in enumerate(arr):
            value_to_idxs[v].append(i)
        
        while queue:
            idx, steps = queue.popleft()

            if idx == target:
                return steps
            
            destinations = [idx+1, idx-1]
            
            destinations.extend(value_to_idxs.pop(arr[idx], []))

            for j in destinations:
                if 0 <= j <= target and j not in visited:
                    visited.add(j)
                    queue.append((j, steps + 1))
        
        return -1
