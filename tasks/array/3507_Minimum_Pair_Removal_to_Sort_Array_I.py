class Solution:
    def minimumPairRemoval(self, nums: list[int]) -> int:
        ans = 0

        flag = True
        while len(nums) > 1:
            pair = float("inf")
            inx = -1
            is_non_descending= True
            for i in range(1,len(nums)):
                if pair > nums[i] + nums[i-1]:
                    inx = i
                    pair = nums[i] + nums[i-1]
                if nums[i-1] > nums[i]:
                    is_non_descending = False
            
            if is_non_descending == True:
                break

            nums[inx-1] = nums[inx] + nums[inx-1]
            nums.pop(inx)
            ans += 1
        
        return ans