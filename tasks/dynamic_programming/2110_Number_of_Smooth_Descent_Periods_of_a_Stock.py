class Solution:
    def getDescentPeriods(self, prices: list[int]) -> int:
        result = 1
        prev = 1
        for i in range(1, len(prices)):
            if prices[i-1] - prices[i] == 1:
                prev += 1
            else:
                prev = 1
            result += prev
        
        return result