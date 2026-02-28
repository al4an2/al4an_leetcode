class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        longest = 0
        set_n = set(nums)
        for num in set_n:
            if num-1 not in set_n:
                next_n = num+1
                curr_len= 1
                while next_n in set_n:
                    curr_len += 1
                    next_n += 1
                longest = max(longest, curr_len)
                    
        return longest