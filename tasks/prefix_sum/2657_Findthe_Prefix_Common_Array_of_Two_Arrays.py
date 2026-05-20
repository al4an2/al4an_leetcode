#set
class Solution:
    def findThePrefixCommonArray(self, A: list[int], B: list[int]) -> list[int]:
        seen = set()
        ans = []
        common = 0

        for a, b in zip(A, B):
            for el in (a, b):
                if el in seen:
                    common += 1
                else:
                    seen.add(el)

            ans.append(common)

        return ans
    
#two defaultdits - works for repitable number in arrays
from collections import defaultdict
class Solution:
    def findThePrefixCommonArray(self, A: list[int], B: list[int]) -> list[int]:
        n = len(A)
        dict_a, dict_b = defaultdict(int), defaultdict(int)
        ans = [0] * n

        for i in range(n):
            a = A[i]
            b = B[i]
            ans[i] = ans[i-1] if i-1 >= 0 else 0
            
            if a == b:
                ans[i] += 1
                continue

            if dict_b[a] > 0:
                ans[i] += 1
                dict_b[a] -= 1
            
            if dict_a[b] > 0:
                ans[i] += 1
                dict_a[b] -= 1
                
            dict_a[a] += 1
            dict_b[b] += 1
        
        return ans