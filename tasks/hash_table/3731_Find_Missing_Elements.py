class Solution:
    def findMissingElements(self, nums: list[int]) -> list[int]:
        ans = []
        st_n = set(nums)
        max_n, min_n = max(st_n), min(st_n)

        
        for num in range(min_n, max_n):
           if num not in st_n:
            ans.append(num)
        
        return ans
