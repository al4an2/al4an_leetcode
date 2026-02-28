class Solution:
    def concatenatedBinary(self, n: int) -> int:
        MOD = 10**9+7

        result = 0
        for num in range(1, n+1):
            len_n = num.bit_length()
            result = ((result << len_n) | num) % MOD

        return result