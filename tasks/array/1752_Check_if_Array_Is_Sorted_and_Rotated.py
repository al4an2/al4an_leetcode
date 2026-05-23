class Solution:
    def check(self, nums: list[int]) -> bool:
        counter = 0
        n = len(nums)
        
        for i in range(n):

            if nums[i] > nums[(i + 1) % n]:
                counter +=1
        
        return counter < 2
        