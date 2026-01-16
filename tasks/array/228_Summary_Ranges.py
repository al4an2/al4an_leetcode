class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        if not nums:
            return []

        n = len(nums)
        result = []

        p = 0
        i = 1
        while i < n:
            if nums[i-1] != nums[i]-1:
                if p == i-1:
                    result.append(str(nums[p]))
                else:
                    result.append(f"{nums[p]}->{nums[i-1]}")
                p = i
            i += 1
            
        if p == n-1:
            result.append(str(nums[p]))
        else:
            result.append(f"{nums[p]}->{nums[i-1]}")

        return result
