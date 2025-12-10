class Solution:
    def countPermutations(self, complexity: list[int]) -> int:
        MOD = 10**9 + 7
        min_complexity = complexity[0]
        result = 1
        for i in range(1,len(complexity)):
            if complexity[i] <= min_complexity:
                return 0
            
            result = result*i % MOD

        return result 