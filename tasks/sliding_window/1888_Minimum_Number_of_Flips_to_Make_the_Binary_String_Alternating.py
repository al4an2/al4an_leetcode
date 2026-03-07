class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        s_double = s + s

        diff1 = 0
        diff2 = 0
        result = float('inf')

        for i in range(len(s_double)):
            
            zero_start = "1" if i % 2 == 0 else "0"
            
            if s_double[i] != zero_start:
                diff1 += 1
            else:
                diff2 += 1
            
            if i >= n:
                pos = i-n
                prev = s_double[pos]
                
                prev_zero_start = "1" if pos % 2 == 0 else "0"

                if prev != prev_zero_start:
                    diff1 -= 1
                else:
                    diff2 -= 1
            
            if i >= n-1:
                result = min(result, diff1, diff2)

        return result