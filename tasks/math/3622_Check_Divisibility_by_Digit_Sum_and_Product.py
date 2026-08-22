class Solution:
    def checkDivisibility(self, n: int) -> bool:
        num = n
        sum_n = 0
        prod_n = 1
        while num > 0:
            digit = num % 10
            num //= 10
            sum_n += digit
            prod_n *= digit

        return n % (sum_n + prod_n) == 0