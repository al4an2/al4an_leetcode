from collections import defaultdict

class Solution:
    def pyramidTransition(self, bottom: str, allowed: list[str]) -> bool:
        
        rules = defaultdict(set)
        for a,b,c in allowed:
            rules[a + b].add(c)

        bad = set()

        def dfs(row, index, nxt):
            if len(row) == 1:
                return True

            if index == len(row) - 1:
                if nxt in bad:
                    return False
                is_ok = dfs(nxt, 0, "")
                if not is_ok:
                    bad.add(nxt)
                return is_ok

            key = row[index:index + 2]
            for c in rules[key]:
                if key not in rules:
                    return False
                if dfs(row, index + 1, nxt + c):
                    return True

            return False

        return dfs(bottom, 0, "")