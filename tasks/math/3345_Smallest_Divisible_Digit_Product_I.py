class Solution:
    def smallestNumber(self, n: int, t: int) -> int:

        while True:
            product = 1
            candidate = n

            while candidate > 0:
                product *= candidate % 10
                candidate //= 10

            if product % t == 0:
                return n

            n += 1
