class Solution:
    def maxDepth(self, s: str) -> int:
        max_depth = 0
        depth = 0
        for el in s:
            if el == '(':
                depth += 1
            elif el == ')':
                depth -= 1
            max_depth = max(max_depth, depth)

        return max_depth