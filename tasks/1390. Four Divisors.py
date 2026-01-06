class Solution:
    def sumFourDivisors(self, nums: list[int]) -> int:
        def sumdiv(n: int):
            div = set()
            for i in range(1, int(n**0.5) + 1):
                if n % i == 0:
                    div.add(i)
                    div.add(n // i)
                if len(div) > 4:
                    return 0
            return sum(div) if len(div) == 4 else 0
        
        result = 0
        for num in nums:
            result += sumdiv(num)
        return result