class Solution:
    def minimumPushes(self, word: str) -> int:
        n = len(word)
        full = n // 8
        end = n % 8

        return(sum([8 * cost for cost in range(1, full + 1)]) + end * (full + 1))