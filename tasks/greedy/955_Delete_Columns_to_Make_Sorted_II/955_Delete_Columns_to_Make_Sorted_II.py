class Solution:
    def minDeletionSize(self, strs: list[str]) -> int:
        n = len(strs)
        count = 0
        cuts = [False] * (n - 1)
        for col in range(len(strs[0])):
            bad = False
            for row in range(1, n):
                if not cuts[row-1] and strs[row][col] < strs[row-1][col]:
                    bad = True
                    break
            
            if bad:
                count += 1
                continue
            
            for row in range(1, n):
                if strs[row][col] > strs[row-1][col]:
                    cuts[row-1] = True

        return count
        