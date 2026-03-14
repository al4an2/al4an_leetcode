class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        def dfs(curr, count):
            if len(curr) == n:
                count += 1
                if count == k:
                    return count, curr
                return count, ""

            for c in ['a', 'b', 'c']:
                if curr and curr[-1] == c:
                    continue

                count, result = dfs(curr + c, count)
                if result:
                    return count, result
                    
            return count, ""

        _, result = dfs("", 0)
        return result