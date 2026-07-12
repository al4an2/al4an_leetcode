class Solution:
    def minDeletionSize(self, strs: list[str]) -> int:
        n = len(strs)
        count = 0
        for i in range(len(strs[0])):
            for j in range(1, n):
                if strs[j][i] < strs[j - 1][i]:
                    count +=1
                    break
        
        return count