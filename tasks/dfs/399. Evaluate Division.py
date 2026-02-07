from collections import defaultdict
class Solution:
    def calcEquation(self, equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:
        graph = defaultdict(dict)

        for i in range(len(equations)):
            start, finish = equations[i][0], equations[i][1]
            graph[start][finish] = values[i]
            graph[finish][start] = 1 / values[i]

        def dfs(current, target, visited, cost):
            if current == target:
                return cost

            visited.add(current)
            for s, c in graph[current].items():
                if s not in visited:
                    res = dfs(s, target, visited, cost * c)
                    if res != -1.0:
                        return res

            return -1.0  

        result = []
        for q in queries:
            if q[0] not in graph or q[1] not in graph:
                result.append(float(-1))
            
            else:
                visited = set()
                result.append(dfs(q[0], q[1], visited, 1.0))
            
        return result