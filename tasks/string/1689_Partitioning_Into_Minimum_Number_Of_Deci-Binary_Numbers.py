#O(n)
class Solution:
    def minPartitions(self, n: str) -> int:
        ans = "0"
        for num in n:
            if num > ans:
                ans = num
            if ans == "9": #microoptimization
                break
        return int(ans)

#python hack O(n)
class Solution:
    def minPartitions(self, n: str) -> int:
        return int(max(n))
    
#fastest, but 9 * O(n)
class Solution:
    def minPartitions(self, n: str) -> int:
        for digit in "987654321":
            if digit in n:
                return int(digit)
