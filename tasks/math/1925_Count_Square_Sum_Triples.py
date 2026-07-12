class Solution:
    def countTriples(self, n: int) -> int:
        c=set([i**2 for i in range(1,n+1)])
        result = 0
        for a in range(1, n+1):
            for b in range(a, n+1):
               if ((a*a)+(b*b)) in c:
                if a == b:
                    result += 1
                else:
                    result += 2
        return result