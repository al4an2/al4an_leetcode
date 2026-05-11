class Solution:
    def separateDigits(self, nums: list[int]) -> list[int]:
        ans = []
        for n in nums:
            for x in str(n):
                ans.append(int(x))
        return ans

#without string manipulation
class Solution:
    def separateDigits(self, nums: list[int]) -> list[int]:
        ans = []

        for i in range(len(nums)-1, -1, -1):
            val = nums[i]
            while val > 0:
                ans.append(val % 10)
                val = val // 10
        ans.reverse()
        return ans